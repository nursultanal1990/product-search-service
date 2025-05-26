from elasticsearch import Elasticsearch

from config.settings import ELASTICSEARCH_HOST


es_client = Elasticsearch(ELASTICSEARCH_HOST)
