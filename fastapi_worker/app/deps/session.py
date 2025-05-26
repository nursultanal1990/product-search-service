from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.db import sqlalchemy_factory


DbSession = Annotated[AsyncSession, Depends(sqlalchemy_factory.get_db_session)]
