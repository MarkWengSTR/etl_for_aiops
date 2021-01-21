anomaly_detect_twaren_device = {
    "job_id": "must assign",
    "job_body": {
        "description": "",
        "groups": [],
        "analysis_config": {
            "bucket_span": "15m",
            "detectors": [
                {
                    "function": "mean",
                    "field_name": "CPUStatus",
                    "partition_field_name": "Devices_name"
                }
            ],
            "influencers": [
                "Devices_name"
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
    "datafeed_id": "must assign",
    "datafeed_body": {
        "job_id": "must assign",
        "indices": ["must assign", ]
    },
    "datafeed_time": {
        "start": "2021-01-21T00:00:00",
    },
    "datafeed_stop_params": None,
    "get_records_params": {
        "sort": "record_score",
        "desc": True
    },
}
