from confluent_kafka import Producer
from loguru import logger
from config.settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_CLIENT_ID


conf = {
    'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS,
    'client.id': KAFKA_CLIENT_ID,
}

producer = Producer(conf)


def delivery_report(err, msg):
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")


def produce(topic, value, key=None):
    try:
        producer.produce(topic, key=key, value=value, callback=delivery_report)
        producer.poll(0)
    except BufferError as e:
        logger.warning("Local producer queue is full, waiting...")
        producer.poll(1)
        produce(topic, value, key)
