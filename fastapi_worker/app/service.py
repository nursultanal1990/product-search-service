from loguru import logger

from app.repo import ProductRepository
from app.schemas import ProductBase


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_product_by_id(
        self,
        product_id: str,
    ) -> ProductBase:
        try:
            return await self.repository.get_product_by_id(
                product_id==product_id,
            )
        except Exception as e:
            logger.error(e)
            raise
