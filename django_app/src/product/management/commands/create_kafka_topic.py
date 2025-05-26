from django.core.management.base import BaseCommand

from confluent_kafka.admin import (
    AdminClient,
    NewTopic,
)

from config.settings import KAFKA_BOOTSTRAP_SERVERS


class Command(BaseCommand):
    help = "Create a Kafka topic if it does not exist"

    def handle(self, *args, **options):
        topic = "product-request"

        conf = {
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS,
        }

        admin_client = AdminClient(conf)
        new_topic = NewTopic(topic=topic, num_partitions=1, replication_factor=1)

        self.stdout.write(f"🔧 Creating topic '{topic}'...")

        fs = admin_client.create_topics([new_topic])

        for t, f in fs.items():
            try:
                f.result()
                self.stdout.write(
                    self.style.SUCCESS(f"✅ Topic '{t}' created successfully."),
                )
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f"⚠️ Topic '{t}' could not be created: {e}"),
                )
