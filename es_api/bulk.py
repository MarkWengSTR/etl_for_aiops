import functools

# documents = [
#     {"index": {"_id": "dev001-1611214501578"}},
#     {
#         "Devices_name": "TWAREN-TP-ASR9912-01",
#         "Devices_id": 1,
#         "CPUStatus": 0,
#         "CPUStatus_CheckTime": 1611214202000,
#         "MemoryStatus": 0,
#         "MemoryStatus_CheckTime": 1611214202000,
#         "TemperatureStatus": 0,
#         "TemperatureStatus_CheckTime": 0,
#         "v4PingStatus": 0,
#         "v4PingStatus_CheckTime": 1611214253000,
#         "v6PingStatus": 0,
#         "VoltageStatus": 0,
#         "VoltageStatus_CheckTime": 0,
#         "CurrentStatus": 0,
#         "CurrentStatus_CheckTime": 0,
#         "CurrentCPU": 9,
#         "CurrentMemory": 30,
#         "CurrentMinRTT": 4.29,
#         "CurrentAvgRTT": 4.39,
#         "CurrentMaxRTT": 4.53,
#         "CurrentPktLossRate": 0,
#         "@timestamp": 1611214501578
#     }
# ]


def single_post_reformat(docu):
    return [
        {"index": {"_id": docu["_id"]}},
        docu["_source"]
    ]


def posts_reformat(documents):
    return list(functools.reduce(lambda collec, docu: collec +
                                 single_post_reformat(docu), documents, []))


def post_from_search(ctx):

    documents = ctx["search_result"]["hits"]["hits"]

    if documents:
        ctx["analy_es_object"].bulk(
            posts_reformat(documents), index=documents[0]["_index"])
    # expect only one index

    return ctx
