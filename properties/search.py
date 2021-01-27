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
                            "gte": "now-15m/m",
                            "lt": "now/m"
                        }
                    }},
                    {"range": {"CurrentCPU": {"lte": 100}}},
                    {"range": {"CurrentMemory": {"lte": 100}}}
                ]
            }
        }
    }
}
# "body": {
#     "size": 10000,
# }
