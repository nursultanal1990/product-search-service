from app.schemas import ProductBase
from loguru import logger
from pypika import (
    Query,
    Table,
)
from sqlalchemy import text


product = Table("product_product")


class ProductRepository:

    def __init__(self, session):
        self.session = session

    async def get_product_by_id(
        self,
        product_id: str,
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
            raw = await self.session.execute(stmt)
            result = raw.mappings().fetchone()

            return ProductBase(**result)

        except Exception as e:
            logger.error(e)
            raise
