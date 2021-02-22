import functools
import csv

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


def reformat_for_bulk(docu):
    return [
        {"index": {"_id": docu["_id"]}},
        docu["_source"]
    ]


def reformat_source(docu):
    return [
        docu["_source"]
    ]


def posts_reformat(documents, reformat_func) -> list:
    return list(functools.reduce(lambda collec, docu: collec +
                                 reformat_func(docu), documents, []))


def bulk_to_csv(ctx):
    documents = ctx["search_result"]

    if documents:
        result = posts_reformat(documents, reformat_source)
        col_names = result[0].keys()

        with open("test.csv", "w", newline="") as out_file:
            dict_writer = csv.DictWriter(out_file, col_names)
            dict_writer.writeheader()
            dict_writer.writerows(result)

    return ctx


def bulk_from_scan(ctx):
    documents = ctx["search_result"]

    if documents:
        ctx["analy_es_object"].bulk(
            posts_reformat(documents, reformat_for_bulk),
            index=ctx.get("index_properties", {}).get("name") or ctx["override_index_name"] or documents[0]["_index"])
    # expect documents have only one index

    return ctx


def bulk_from_search(ctx):
    documents = ctx["search_result"]["hits"]["hits"]

    if documents:
        ctx["analy_es_object"].bulk(
            posts_reformat(documents, reformat_for_bulk),
            index=ctx.get("index_properties", {}).get("name") or ctx["override_index_name"] or documents[0]["_index"])
    # expect documents have only one index

    return ctx
