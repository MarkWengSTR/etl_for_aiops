import es_api.object as ob
import es_api.index as idx
import es_api.ml_anomaly_detection as mlad
import data.object as es_ob_prop
import es_api.search as es_search
import logging
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
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
        },
        "close_job_params": None,
        "datafeed_id": "datafeed-cpu-data-python",
        "datafeed_body": {
            "job_id": "20201123-cpu-reqtest-python",
            "indices": ["20201123-cpu-data"]
        },
        "datafeed_time": {
            "tart": "2020-11-23T00:00:16Z",
        },
        "datafeed_stop_params": None,
        "get_records_params": {
            "sort": "record_score",
            "desc": True
        },
    }

    search_asr_device = {
        "index": "nms-devices_status-test-2020.07",
        "body": {
            "size": 100,
            "query": {
                "bool": {
                    "must": [
                        {"regexp": {
                            "Devices_name.keyword": {
                                "value": ".*ASR.*"
                            }
                        }}
                    ],
                    "filter": [
                        {"range": {
                            "@timestamp": {
                                "gte": "now-5m/m",
                                "lt": "now/m"
                            }
                        }}
                    ]
                }
            }
        }
    }

    ctx = {
        "es_object": None,
        "es_properties": es_ob_prop.data_es,
        "index_properties": index_properties,
        "mlad_properties": mlad_properties,
        "search_properties": search_asr_device,
        "search_result": None,
        "mlad_result": None
    }

    # ob.prepare_es_object(ctx) and \
    #     idx.create_process(ctx)
    # ob.prepare_es_object(ctx) and \
    #     mlad.process(ctx)
    ob.prepare_es_object(ctx) and \
        es_search.process(ctx)
