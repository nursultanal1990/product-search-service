from loguru import logger
from pypika import Query, Table
from sqlalchemy import text

from app.deps import DbSession
from app.schemas import ProductBase


product = Table("product")


async def get_product_by_id(
    product_id: str,
    session: DbSession,
) -> ProductBase:
    try:
        q = (
            Query.from_(product)
            .select(
                product.id,
                product.name,
                product.description,
                product.created_at,
            )
            .where(product.id == product_id)
        )

        stmt = text(q.get_sql())
        raw = await session.execute(stmt)
        result = raw.mappings().fetchone()

        return ProductBase(**result)

    except Exception as e:
        logger.error(e)
        raise
