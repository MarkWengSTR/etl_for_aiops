twaren_asr_device = {
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
