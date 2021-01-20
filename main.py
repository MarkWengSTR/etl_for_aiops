import es_api.object as ob
import es_api.index as idx
import es_api.machine_learning.anomaly_detection as mlad
import properties.object as es_ob_prop
import properties.index as es_idx_prop
import properties.machine_learning as es_ml_prop
import properties.search as es_search_prop
import es_api.search as es_search
import logging
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    ctx = {
        "es_object": None,
        "created_new_index": None,
        "es_properties": es_ob_prop.ml_es,
        "index_properties": es_idx_prop.twaren_device,
        "mlad_properties": es_ml_prop.anomaly_detect_twaren_device,
        "search_properties": es_search_prop.twaren_asr_device,
        "search_result": None,
        "mlad_result": None
    }

    ob.prepare_es_object(ctx) and \
        idx.create_process(ctx)
    # ob.prepare_es_object(ctx) and \
    #     mlad.process(ctx)
    # ob.prepare_es_object(ctx) and \
    #     es_search.process(ctx)
