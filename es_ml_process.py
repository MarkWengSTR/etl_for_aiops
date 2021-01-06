from elasticsearch import Elasticsearch


def prepare_es_object(ctx):
    es_setting = ctx["es_setting"]
    es_setting["es_object"] = Elasticsearch(
        es_setting["end_point"], http_auth=(
            es_setting["user"], es_setting["password"])
    )

    return ctx


def prepare_index(ctx):
    index_body = ctx["index_setting_struc"]["body"]
    index_properties = ctx["index_properties"]

    index_body["settings"]["number_of_shards"] = index_properties["shards"]
    index_body["settings"]["number_of_replicas"] = index_properties["replicas"]
    index_body["mappings"]["properties"] = index_properties["properties"]

    return ctx


def create_index(ctx):
    es = ctx["es_setting"]["es_object"]

    result = es.indices.create(
        index=ctx["index_properties"]["name"], body=ctx["index_setting_struc"]["body"])
    print(result)

    return ctx


if __name__ == "__main__":
    es_setting = {
        "end_point": "https://4b90f7555cf24f80878d2e9144d04507.asia-east1.gcp.elastic-cloud.com:9243",
        "user": "elastic",
        "password": "uChHjfYU1WX6CM2KCkZqzESB",
        "es_object": None,
    }

    index_setting_struc = {
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
    }

    index_properties = {
        "name": "2021-01-06-test",
        "shards": 1,
        "replicas": 1,
        "properties": {
            "Datetime": {"type": "date"},
            "Devices_name": {"type": "text"},
            "memory": {"type": "float"}
        }
    }

    ctx = {
        "es_setting": es_setting,
        "index_setting_struc": index_setting_struc,
        "index_properties": index_properties,
    }

    prepare_es_object(ctx) and \
        prepare_index(ctx) and \
        create_index(ctx)
