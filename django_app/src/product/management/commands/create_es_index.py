from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from config.settings import ELASTICSEARCH_HOST


class Command(BaseCommand):
    help = "Creates the 'products' index in es with proper mappings."

    def handle(self, *args, **options):
        es = Elasticsearch(ELASTICSEARCH_HOST)

        index_name = "products"

        mappings = {
            "properties": {
                "id": {"type": "keyword"},
                "name": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    }
                },
                "description": {"type": "text"},
                "created_at": {
                    "type": "date",
                    "format": "strict_date_optional_time||epoch_millis"
                }
            }
        }

        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, mappings=mappings)
            self.stdout.write(self.style.SUCCESS(f"Index '{index_name}' created successfully."))
        else:
            self.stdout.write(self.style.WARNING(f"Index '{index_name}' already exists."))
