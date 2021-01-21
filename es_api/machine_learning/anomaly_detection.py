from elasticsearch.client import MlClient


def create_job(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    MlClient.put_job(
        mlad_ctx["es_object"], job_id=mlad_properties["job_id"], body=mlad_properties["job_body"])

    return mlad_ctx


def open_job(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    MlClient.open_job(mlad_ctx["es_object"],
                      job_id=mlad_properties["job_id"])

    return mlad_ctx


def close_job(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    MlClient.close_job(mlad_ctx["es_object"],
                       job_id=mlad_properties["job_id"])

    return mlad_ctx


def create_datafeed(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]
    datafeed_body = {
        "job_id": mlad_properties["job_id"],
        "indices": mlad_properties["datafeed_body"]["indices"]
    }

    MlClient.put_datafeed(
        mlad_ctx["es_object"], datafeed_id=mlad_properties["datafeed_id"], body=datafeed_body)

    return mlad_ctx


def start_datafeed(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    MlClient.start_datafeed(
        mlad_ctx["es_object"], datafeed_id=mlad_properties["datafeed_id"], body=mlad_properties["datafeed_time"])

    return mlad_ctx


def stop_datafeed(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    MlClient.stop_datafeed(
        mlad_ctx["es_object"], datafeed_id=mlad_properties["datafeed_id"], body=mlad_properties["datafeed_stop_params"])

    return mlad_ctx


def get_records(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    result = MlClient.get_records(
        mlad_ctx["es_object"], job_id=mlad_properties["job_id"], body=mlad_properties["get_records_params"])

    """
    {"count":904,"records":[
        {'job_id': '20201123-cpu-reqtest',
         'result_type': 'record',
         'probability': 7.98024424988483e-61,
         'multi_bucket_impact': -5.0,
         'record_score': 98.77009619528458,
         'initial_record_score': 98.77009619528458,
         'bucket_span': 900,
         'detector_index': 0,
         'is_interim': False,
         'timestamp': 1606423500000,
         'partition_field_name': 'hostname',
         'partition_field_value': 'TANet-CCU-ASR9010-01',
         'function': 'mean',
         'function_description': 'mean',
         'typical': [2.6715904907637635],
         'actual': [86.33333333333334],
         'field_name': 'cpu',
         'influencers': [{'influencer_field_name': 'hostname',
           'influencer_field_values': ['TANet-CCU-ASR9010-01']}],
         'hostname': ['TANet-CCU-ASR9010-01']}
    ]}
    """

    mlad_ctx["ad_result"] = result
    return mlad_ctx


def process(ctx):
    mlad_ctx = {
        "es_object": ctx["analy_es_object"],
        "mlad_properties": ctx["mlad_properties"],
        "ad_result": None
    }

    create_job(mlad_ctx) and \
        create_datafeed(mlad_ctx) and \
        open_job(mlad_ctx) and \
        start_datafeed(mlad_ctx)

    # get_records(mlad_ctx) # get ml analysis result
    # ctx["mlad_result"] = mlad_ctx["ad_result"]

    return ctx
