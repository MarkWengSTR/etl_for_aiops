import es_api.object as ob
import es_api.index as idx
import es_api.search as es_search
import es_api.bulk as es_bulk
import properties.index as es_idx_prop
import properties.search as es_search_prop
import logging
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    for day_range in es_search.days_range_props_list(15):
        search_properties = es_search.replace_range_prop(
            es_search_prop.twaren_asr_device, day_range)

        ctx = {
            "data_es_object": None,
            "analy_es_object": None,
            "is_created_new_index": None,
            "index_properties": es_idx_prop.twaren_device,
            "search_properties": search_properties,
            "search_result": None,
        }

        ob.prepare_all(ctx) and \
            idx.create_process(ctx) and \
            es_search.scan(ctx) and \
            es_bulk.bulk_from_scan(ctx)
