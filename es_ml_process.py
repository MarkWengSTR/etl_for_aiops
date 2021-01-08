import es_api.object as ob
import es_api.index as idx
import es_api.ml_anomaly_detection as mlad


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

    mlad_properties = {
        "job_id": "20201123-cpu-reqtest-python",
        "job_body": {
            "description": "",
            "groups": [],
            "analysis_config": {
                  "bucket_span": "15m",
                "detectors": [
                    {
                        "function": "mean",
                        "field_name": "cpu",
                        "partition_field_name": "hostname"
                    }
                ],
                "influencers": [
                    "hostname"
                ]
            },
            "data_description": {
                "time_field": "@timestamp"
            },
            "custom_settings": {
                "created_by": "multi-metric-wizard"
            },
            "analysis_limits": {
                "model_memory_limit": "13MB"
            },
            "model_plot_config": {
                "enabled": False,
                "annotations_enabled": False
            }
        }
    }

    ctx = {
        "es_object": None,
        "es_properties": es_properties,
        "index_properties": index_properties,
        "mlad_properties": mlad_properties
    }

    # ob.prepare_es_object(ctx) and \
    #     idx.create_process(ctx)
    ob.prepare_es_object(ctx) and \
        mlad.mlad_process(ctx)
