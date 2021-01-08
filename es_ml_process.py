import es_api.index as idx
import es_api.object as ob


if __name__ == "__main__":
    es_properties = {
        "end_point": "https://afa935ed198c480d8d9d7a58a60eadb7.asia-east1.gcp.elastic-cloud.com:9243",
        "user": "elastic",
        "password": "quSvDoseZIgR4KhD9fCS6UN4",
    }

    index_properties = {
        "name": "2021-01-08-test",
        "shards": 1,
        "replicas": 1,
        "properties": {
            "Datetime": {"type": "date"},
            "Devices_name": {"type": "text"},
            "memory": {"type": "float"}
        }
    }

    ctx = {
        "es_object": None,
        "es_properties": es_properties,
        "index_properties": index_properties,
    }

    ob.prepare_es_object(ctx) and \
        idx.create_process(ctx)
