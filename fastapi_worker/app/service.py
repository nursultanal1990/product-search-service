from loguru import logger
from elasticsearch import AsyncElasticsearch

from app.config import settings
from app.repo import ProductRepository
from app.db import sqlalchemy_factory as sqla


es = AsyncElasticsearch(settings.elasticsearch_host)


async def update_product_cache(
    product_id: str,
):
    try:
        async for session in sqla.get_db_session():
            repo = ProductRepository(session)
            product = await repo.get_product_by_id(product_id)
            logger.info(product)

            if not product:
                logger.warning(f"Product {product_id} not found in DB")
                return

            doc = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "created_at": product.created_at.isoformat() if product.created_at else None
            }

            logger.info(f"es doc: {doc}")

            await es.index(index="products", id=product.id, document=doc)
            logger.info(f"Product {product_id} indexed in es")

    except Exception as e:
        logger.error(e)
