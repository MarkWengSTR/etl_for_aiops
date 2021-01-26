import elasticsearch.helpers


def scan(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = list(
        elasticsearch.helpers.scan(
            es, index=search_properties["index"], preserve_order=True, query=search_properties["body"]))

    return ctx


def execute(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = es.search(
        index=search_properties["index"], body=search_properties["body"])

    return ctx
