def search(search_ctx):
    es = search_ctx["es_object"]

    search_ctx["result"] = es.search(
        index=search_ctx["search_properties"]["index"], body=search_ctx["search_properties"]["body"])

    return search_ctx


def process(ctx):
    search_ctx = {
        "es_object": ctx["es_object"],
        "search_properties": ctx["search_properties"],
        "result": None
    }

    search(search_ctx)

    ctx["search_result"] = search_ctx["result"]

    return ctx
