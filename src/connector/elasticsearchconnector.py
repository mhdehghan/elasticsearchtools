from elasticsearch import Elasticsearch


class ElasticsearchConnector:

    def __init__(self, elasticsearch_config, http_auth):
        self.elasticsearch_config = elasticsearch_config
        self.http_auth = http_auth

    def get_es_instance(self):
        return Elasticsearch(self.elasticsearch_config.get('host_port'), http_auth=self.http_auth)
