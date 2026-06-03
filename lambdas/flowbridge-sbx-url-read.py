import json
import logging
from datetime import datetime, timezone
import os 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

rds_host = os.getenv("RDS_HOST")
def lambda_handler(event, context):

    logger.info("flowbridge-sbx-url-read invoked")
    logger.info("Event: %s", json.dumps(event))

    query_params = event.get("queryStringParameters") or {}

    response_body = {
        "message": "Test Eugin URL Read Lambda",
        "lambda_name": "flowbridge-sbx-url-read",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "query_params": query_params,
        "received_event": event
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(response_body)
    }