anomaly_detect_twaren_device = {
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
        "start": "2020-11-23T00:00:16Z",
    },
    "datafeed_stop_params": None,
    "get_records_params": {
        "sort": "record_score",
        "desc": True
    },
}
