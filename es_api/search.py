def execute(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = es.search(
        index=search_properties["index"], body=search_properties["body"])

    return ctx
