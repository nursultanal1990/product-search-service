import json
from loguru import logger

from faststream.kafka import KafkaBroker, KafkaMessage
from fastapi import Depends
from sqlalchemy.future import select

from elasticsearch import AsyncElasticsearch

from app.config import settings
from app.deps import DbSession, get_es_client
from app.service import get_product_by_id


broker = KafkaBroker(settings.kafka_bootstrap_servers)


@broker.subscriber("product-request")
async def handle_kafka_event(
    msg: KafkaMessage,
    es: AsyncElasticsearch = Depends(get_es_client),
):
    try:
        data = json.loads(msg.body.decode())
        product_id = data["product_id"]
        logger.info(f"Received product_id: {product_id}")

        result = await get_product_by_id(product_id=product_id)
        product = result.scalar_one_or_none()

        if not product:
            logger.warning(f"Product {product_id} not found in DB")
            return

        doc = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "created_at": product.created_at.isoformat() if product.created_at else None
        }

        await es.index(index="products", id=product.id, document=doc)
        logger.info(f"Product {product_id} indexed in es")
    except Exception as e:
        logger.error(e)
