def is_exist(index_ctx):
    return index_ctx["es_object"].indices.exists(
        index=index_ctx["index_properties"]["name"])


def prepare(index_ctx):
    index_body = index_ctx["index_setting_struc"]["body"]
    index_properties = index_ctx["index_properties"]

    index_body["settings"]["number_of_shards"] = index_properties["shards"]
    index_body["settings"]["number_of_replicas"] = index_properties["replicas"]
    index_body["mappings"]["properties"] = index_properties["properties"]

    return index_ctx


def create(index_ctx):
    es = index_ctx["es_object"]

    result = es.indices.create(
        index=index_ctx["index_properties"]["name"], body=index_ctx["index_setting_struc"]["body"])
    print(result)

    return index_ctx


def create_process(ctx):
    index_ctx = {
        "index_setting_struc": {
            "name": "",
            "body": {
                "settings": {
                    "number_of_shards": None,
                    "number_of_replicas": None
                },
                "mappings": {
                    "properties": {}
                }
            }
        },
        "es_object": ctx["es_object"],
        "index_properties": ctx["index_properties"],
    }

    if is_exist(index_ctx):
        ctx["index_already_exist"] = True
    else:
        ctx["index_already_exist"] = False
        prepare(index_ctx) and \
            create(index_ctx)

    return ctx
