import json

def lambda_handler(event, context):
    print("url-lambda event:", json.dumps(event))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "url lambda working eugin twdwdest"
        })
    }
