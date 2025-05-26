from contextlib import asynccontextmanager

from app.kafka_worker import broker
from fastapi import FastAPI
from loguru import logger


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
