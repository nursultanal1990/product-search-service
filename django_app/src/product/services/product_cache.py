from elasticsearch import NotFoundError
from product.services.es_client import es_client
from product.services.kafka_producer import produce
from loguru import logger
import json


def get_product_from_cache(
    product_id: str,
    index: str = "products"
) -> dict | None:
    try:
        result = es_client.get(index=index, id=product_id)
        return result["_source"]
    except NotFoundError:
        return None
    except Exception as e:
        logger.error(f"[Elasticsearch] Unexpected error: {e}")
        return None


def get_or_request_product(
    product_id: str,
    index: str = "products",
    topic: str = "product-request"
) -> dict | None:
    product = get_product_from_cache(product_id, index=index)

    if product:
        return product

    event = {
        "event": "product_cache_miss",
        "product_id": product_id
    }

    produce(topic, value=json.dumps(event), key=product_id)
    logger.info(f"Product {product_id} not found in cache. Event sent to Kafka.")

    return None
