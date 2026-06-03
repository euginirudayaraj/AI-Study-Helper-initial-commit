import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    FlowBridge SBX URL Read Lambda.
    This is a sample Lambda handler for testing GitHub -> CodeBuild -> Lambda deployment.
    """

    logger.info("flowbridge-sbx-url-read invoked")
    logger.info("Event: %s", json.dumps(event))

    query_params = event.get("queryStringParameters") or {}

    response_body = {
        "message": "flowbridge-sbx-url-read Lambda deployed successfully",
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