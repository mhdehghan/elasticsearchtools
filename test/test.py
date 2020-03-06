import yaml

from src.connector.elasticsearchconnector import ElasticsearchConnector
from src.restapi.documentapi.documentapi import delete_index, bulk_query
from src.utility.textutilities import random_string, random_digit


def load_config():
    with open('config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        return config


elasticsearch_config = load_config()
http_auth = (
    elasticsearch_config['elasticsearch']['elastic_user'], elasticsearch_config['elasticsearch']['elastic_pass'])
index_name = elasticsearch_config['elasticsearch']['index_name']


def data_generator(rng=10):
    for i in range(rng):
        my_dic = {'fullname': random_string(), 'id': random_digit()}
        yield {
            "_index": index_name,
            "_type": "_doc",
            **my_dic
        }

#TODO: Write a unit-test!
if __name__ == "__main__":
    load_config()
    while True:
        choice = input("Enter 1 (write documents into an index), 2 (delete an index): ")
        if choice.__eq__('1'):
            elk_connector = ElasticsearchConnector(elasticsearch_config=elasticsearch_config,
                                                   http_auth=http_auth)
            print(bulk_query(elk_connector.get_es_instance(), data_generator()))

        elif choice.__eq__('2'):
            elk_connector = ElasticsearchConnector(elasticsearch_config=elasticsearch_config,
                                                   http_auth=http_auth)
            delete_index(elk_connector.get_es_instance(), index_name)

        elif choice.__eq__('3'):
            break
