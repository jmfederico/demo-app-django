import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pd_django_demo.settings")
django.setup(set_prefix=False)


def get_sqs_event_handler():
    from tasks.sqs import task_sqs_event_handler

    return task_sqs_event_handler


sqs_event_handler = get_sqs_event_handler()
