from elasticsearch import helpers


def post_from_search(ctx):
    documents = ctx["search_result"]["hits"]["hits"]

    if documents:
        helpers.bulk(ctx["analy_es_object"], documents)

    return ctx
