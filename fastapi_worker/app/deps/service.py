from typing import Annotated

from fastapi import Depends

from app.service import ProductService


ProductServiceDep = Annotated[ProductService, Depends()]
