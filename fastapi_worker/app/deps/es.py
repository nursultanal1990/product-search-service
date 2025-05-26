from elasticsearch import AsyncElasticsearch
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings


async def get_es_client() -> AsyncElasticsearch:
    return AsyncElasticsearch(hosts=[settings.elasticsearch_host])
