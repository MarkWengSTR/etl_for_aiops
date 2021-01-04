from elasticsearch import Elasticsearch

def prepare_es_object(ctx):
    es_setting = ctx["es_setting"]
    es_setting["es_object"] = Elasticsearch(es_setting["end_point"], http_auth=(es_setting["user"], es_setting["password"]))

    return data

if __name__ == "__main__":
    ctx = {
        "es_setting": {
            "end_point": "https://de8cee7f68e548459935e317a84be9e5.asia-east1.gcp.elastic-cloud.com:9243",
            "user": "elastic",
            "password": "uChHjfYU1WX6CM2KCkZqzESB",
            "es_object": None,
        }
    }
