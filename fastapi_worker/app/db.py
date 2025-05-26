from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from app.config import settings


class SQLAlchemyFactory:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        pool_size: int = 10,
        max_overflow: int = 5,
        pool_recycle: int = 1800,
        pool_pre_ping: bool = True,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_recycle=pool_recycle,
            pool_pre_ping=pool_pre_ping,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
        )

    async def get_db_session(self) -> AsyncGenerator[AsyncSession, None]:
        from sqlalchemy import exc

        session: AsyncSession = self.session_factory()

        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def dispose(self) -> None:
        await self.engine.dispose()


sqlalchemy_factory = SQLAlchemyFactory(url=settings.database_url)
