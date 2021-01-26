twaren_asr_device = {
    "index": "nms-devices_status-test-2020.07",
    "body": {
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
                            "gte": "now-30m/m",
                            "lt": "now/m"
                        }
                    }}
                ]
            }
        }
    }
}
# "body": {
#     "size": 10000,
# }
