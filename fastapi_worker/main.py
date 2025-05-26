from loguru import logger

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.config import settings
from app.kafka_worker import broker


@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    logger.info("Kafka broker started")

    yield

    await broker.close()
    logger.info("Kafka broker stopped")


app = FastAPI(
    title="FastAPI Worker",
    docs_url="/api/docs",
    debug=True,
    lifespan=lifespan,
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
