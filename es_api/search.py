import elasticsearch.helpers
import functools


def days_range_props_list(days=0):
    # [
    #     {"gte": "now/d", "lt": "now+1d/d"}, -> days=0
    #     {"gte": "now-1d/d", "lt": "now-0d/d"}, -> days=1
    #     {"gte": "now-2d/d", "lt": "now-1d/d"}, -> days=2
    #     {"gte": "now-3d/d", "lt": "now-2d/d"},
    #     {"gte": "now-4d/d", "lt": "now-3d/d"},
    #     ...
    # ]
    return list(
        functools.reduce(
            lambda collec, day: collec +
            [{
                "gte": "now-{0}d/d".format(day+1),
                "lt": "now-{0}d/d".format(day)
            }],
            list(range(days)),
            [{
                "gte": "now/d",
                "lt": "now+1d/d"
            }]
        ))


def replace_range_prop(search_properties, day_prop):
    search_properties["body"]["query"]["bool"]["filter"][0]["range"]["@timestamp"] = day_prop

    print(search_properties)
    return search_properties


def scan(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = list(
        elasticsearch.helpers.scan(
            es, index=search_properties["index"], preserve_order=True, query=search_properties["body"]))

    return ctx


def execute(ctx):
    es = ctx["data_es_object"]
    search_properties = ctx["search_properties"]

    ctx["search_result"] = es.search(
        index=search_properties["index"], body=search_properties["body"])

    return ctx
