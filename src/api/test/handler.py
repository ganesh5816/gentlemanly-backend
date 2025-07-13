import json
def handler(event, context):
    body = {
        "message": "Go Serverless v3.0! Your pipeline us sucess!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
