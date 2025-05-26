from typing import Annotated

from fastapi import Depends

from app.repo import ProductRepository


ProductRepositoryDep = Annotated[ProductRepository, Depends()]
