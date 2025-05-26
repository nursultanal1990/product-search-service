from typing import Annotated

from fastapi import Depends
from elasticsearch import AsyncElasticsearch
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import sqlalchemy_factory
from app.config import settings


DbSession = Annotated[AsyncSession, Depends(sqlalchemy_factory.get_db_session)]


async def get_es_client() -> AsyncElasticsearch:
    es = AsyncElasticsearch(hosts=[settings.elasticsearch_host])
    try:
        yield es
    finally:
        await es.close()
