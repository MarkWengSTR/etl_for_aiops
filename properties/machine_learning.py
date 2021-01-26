anomaly_detect_twaren_device = {
    "job_id": "must assign",
    "job_body": {
        "description": "",
        "groups": [],
        "analysis_config": {
            "bucket_span": "5m",
            "detectors": [
                {
                    "function": "count",
                    "partition_field_name": "Devices_name.keyword"
                },
                {
                    "function": "mean",
                    "field_name": "CurrentCPU",
                    "partition_field_name": "Devices_name.keyword"
                }
            ],
            "influencers": [
                "Devices_name.keyword"
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
        },
        "results_index_name": "same as job id"
    },
    "close_job_params": None,
    "datafeed_id": "must assign",
    "datafeed_body": {
        "job_id": "must assign",
        "indices": "must assign",
        "frequency": "5m",
        "delayed_data_check_config": {
            "enabled": True,
            "check_window": "5m"
        },
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
