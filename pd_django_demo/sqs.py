import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pd_django_demo.settings")
django.setup(set_prefix=False)


def get_lambda_sqs_event_handler():
    from tasks.sqs import task_lambda_sqs_event_handler

    return task_lambda_sqs_event_handler


lambda_sqs_event_handler = get_lambda_sqs_event_handler()
