from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.db import sqlalchemy_factory


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await sqlalchemy_factory.dispose()


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Worker",
        docs_url="/api/docs",
        debug=eval(settings.debug),
        lifespan=lifespan,
    )

    return app
