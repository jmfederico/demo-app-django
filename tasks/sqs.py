from uuid import UUID

import boto3

def task_lambda_sqs_event_handler(event, context):
    from .helpers import complete_task

    for record in event["Records"]:
        task_uuid = record["body"]
        try:
            UUID(task_uuid)
        except ValueError:
            return

        complete_task(task_uuid)


def task_sqs_handler(message):
    from .helpers import complete_task

    task_uuid = message["Body"]
    try:
        UUID(task_uuid)
    except ValueError:
        return

    complete_task(task_uuid)
