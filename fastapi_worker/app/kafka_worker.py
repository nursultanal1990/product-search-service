import json
from loguru import logger

from faststream.kafka import KafkaBroker, KafkaMessage

from app.config import settings
from app.db import sqlalchemy_factory as sqla
from app.service import update_product_cache


broker = KafkaBroker(settings.kafka_bootstrap_servers)


@broker.subscriber("product-request")
async def handle_kafka_event(msg: KafkaMessage):
    try:
        data = json.loads(msg.body.decode())
        product_id = data["product_id"]
        logger.info(f"Received product_id: {product_id}")

        await update_product_cache(product_id=product_id)

    except Exception as e:
        logger.error(e)
