from elasticsearch import Elasticsearch


def prepare_es_object(ctx):
    es_properties = ctx["es_properties"]
    ctx["es_object"] = Elasticsearch(
        es_properties["end_point"], http_auth=(
            es_properties["user"], es_properties["password"])
    )

    return ctx
