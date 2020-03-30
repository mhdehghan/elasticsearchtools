from elasticsearch import helpers, Elasticsearch


def create_index(es: Elasticsearch, index: str, ignore=400):
    '''
    This function creates an index in Elasticsearch.
    :param es: Input connection
    :param index: Index name
    :param ignore: Types of error that could be ignored
    :return:
    '''
    return es.indices.create(index, ignore=ignore)


def delete_index(es: Elasticsearch, index: str, ignore=[400, 401]):
    '''
    This function deletes an index.
    :param es: Input connection
    :param index: Index name
    :param ignore: Types of error that could be ignored
    :return:
    '''
    return es.indices.delete(index, ignore=ignore)


def bulk_query(es, data):
    return helpers.bulk(es, data)
