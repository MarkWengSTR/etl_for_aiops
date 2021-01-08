from elasticsearch import Elasticsearch
import es_api.index as idx


def prepare_es_object(ctx):
    es_setting = ctx["es_setting"]
    es_setting["es_object"] = Elasticsearch(
        es_setting["end_point"], http_auth=(
            es_setting["user"], es_setting["password"])
    )

    return ctx


if __name__ == "__main__":
    es_setting = {
        "end_point": "https://afa935ed198c480d8d9d7a58a60eadb7.asia-east1.gcp.elastic-cloud.com:9243",
        "user": "elastic",
        "password": "quSvDoseZIgR4KhD9fCS6UN4",
        "es_object": None,
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
        "index_properties": index_properties,
    }

    prepare_es_object(ctx) and \
        idx.create_process(ctx)
