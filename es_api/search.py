import datetime

"""
"mappings": {
    "properties": {
        "@timestamp": {
            "type": "date"
        },
        "CPUStatus": {
            "type": "long"
        },
        "CPUStatus_CheckTime": {
            "type": "date"
        },
        "Channel1_CurrentTemperature": {
            "type": "float"
        },
        "Channel2_CurrentTemperature": {
            "type": "float"
        },
        "Channel3_CurrentTemperature": {
            "type": "float"
        },
        "Channel4_CurrentTemperature": {
            "type": "long"
        },
        "CurrentAvgRTT": {
            "type": "float"
        },
        "CurrentCPU": {
            "type": "long"
        },
        "CurrentMaxRTT": {
            "type": "float"
        },
        "CurrentMemory": {
            "type": "long"
        },
        "CurrentMinRTT": {
            "type": "float"
        },
        "CurrentPktLossRate": {
            "type": "long"
        },
        "CurrentStatus": {
            "type": "long"
        },
        "CurrentStatus_CheckTime": {
            "type": "date"
        },
        "Devices_id": {
            "type": "long"
        },
        "Devices_name": {
            "type": "text",
            "fields": {
                "keyword": {
                    "type": "keyword",
                    "ignore_above": 256
                }
            }
        },
        "MemoryStatus": {
            "type": "long"
        },
        "MemoryStatus_CheckTime": {
            "type": "date"
        },
        "TemperatureStatus": {
            "type": "long"
        },
        "TemperatureStatus_CheckTime": {
            "type": "date"
        },
        "VoltageStatus": {
            "type": "long"
        },
        "VoltageStatus_CheckTime": {
            "type": "date"
        },
        "v4PingStatus": {
            "type": "long"
        },
        "v4PingStatus_CheckTime": {
            "type": "date"
        },
        "v6PingStatus": {
            "type": "long"
        }
    }
}
"""

EPOCH_FIELDS = [
    "@timestamp", "CPUStatus_CheckTime", "CurrentStatus_CheckTime", "v4PingStatus_CheckTime",
    "VoltageStatus_CheckTime", "TemperatureStatus_CheckTime", "MemoryStatus_CheckTime"
]


def transform_date_field(search_result):
    for document in search_result["hits"]["hits"]:
        for epoch_field in EPOCH_FIELDS:
            document["_source"][epoch_field] = epoch_millis_to_datedime(
                document["_source"][epoch_field])

    return search_result


def epoch_millis_to_datedime(epoch_milliseconds):
    return datetime.datetime.fromtimestamp(
        epoch_milliseconds / 1000.0).strftime('%Y-%m-%d %H:%M:%S')


def execute(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = transform_date_field(
        es.search(index=search_properties["index"], body=search_properties["body"]))
    # ctx["search_result"] = es.search(
    #     index=search_properties["index"], body=search_properties["body"])

    return ctx
