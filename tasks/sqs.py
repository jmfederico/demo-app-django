from uuid import UUID


def task_sqs_event_handler(event, context):
    from .helpers import complete_task

    for record in event["Records"]:
        task_uuid = record["body"]
        try:
            UUID(task_uuid)
        except ValueError:
            return

        complete_task(task_uuid)
