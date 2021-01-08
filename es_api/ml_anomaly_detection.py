from elasticsearch.client import MlClient


def create_job(mlad_ctx):
    mlad_properties = mlad_ctx["mlad_properties"]

    MlClient.put_job(
        mlad_ctx["es_object"], job_id=mlad_properties["job_id"], body=mlad_properties["job_body"])

    return mlad_ctx


def mlad_process(ctx):
    mlad_ctx = {
        "es_object": ctx["es_object"],
        "mlad_properties": ctx["mlad_properties"]
    }

    create_job(mlad_ctx)

    return ctx
