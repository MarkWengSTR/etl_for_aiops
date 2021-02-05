import properties.search as es_search_prop
import es_api.bulk as es_bulk
import es_api.search as es_search
import es_api.object as ob
import logging
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    for hour_range in es_search.time_range_from_now_props_list("h", 97):
        search_properties = es_search.replace_range_prop(
            es_search_prop.twaren_asr_syslog, hour_range)

        ctx = {
            "data_es_object": None,
            "analy_es_object": None,
            "is_created_new_index": None,
            "search_properties": search_properties,
            "search_result": None,
        }

        ob.prepare_all(ctx) and \
            es_search.scan(ctx) and \
            es_bulk.bulk_from_scan(ctx)
