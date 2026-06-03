import json

def lambda_handler(event, context):
    print("url-lambda event:", json.dumps(event))
    return {
        "statusCode": 200,
        "body": json.dumps({fef
            "message": "url lambda working eugin test"
        })
    }
