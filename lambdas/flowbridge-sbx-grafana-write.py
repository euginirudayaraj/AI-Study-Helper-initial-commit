import json
import logging
from datetime import datetime, timezone
import os

test=os.getenv("TEST_ENV_VAR", "default_value")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    FlowBridge SBX Grafana Write Lambda.
    This is a sample Lambda handler for testing GitHub -> CodeBuild -> Lambda deployment.
    """

    logger.info("flowbridge-sbx-grafana-write invoked")
    logger.info("Event: %s", json.dumps(event))

    response_body = {
        "message": "Eugin test",
        "lambda_name": "flowbridge-sbx-grafana-write",
        "timestamp": datetime.now(timezone.utc).isoformat(),
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