from elasticsearch import helpers, Elasticsearch


def create_index(es: Elasticsearch, index: str, ignore=400):
    return es.indices.create(index, ignore=ignore)


def delete_index(es: Elasticsearch, index: str, ignore=[400, 401]):
    return es.indices.delete(index, ignore=ignore)


def bulk_query(es, data):
    return helpers.bulk(es, data)
