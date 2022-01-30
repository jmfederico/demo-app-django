import os
import sys
from time import sleep

import boto3
from django.conf import settings
from django.core.management.base import BaseCommand

from tasks.sqs import task_sqs_handler

client = boto3.client("sqs", endpoint_url=os.environ.get("BOTO_ENDPOINT_URL"))


class Command(BaseCommand):
    help = "Consume the SQS queue and handle messages as they are received."

    def handle(self, *args, **options):
        """Start an SQS consumer, and pass messages to the task handler."""
        self.stdout.write(
            self.style.SUCCESS("Consuming SQS messages from %s" % settings.SQS_URL)
        )
        try:
            while True:
                if not self._handle():
                    sleep(5)
        except KeyboardInterrupt:
            sys.exit(0)

    def _handle(self):
        self.stdout.write(self.style.WARNING("Receiving messages"))
        response = client.receive_message(
            QueueUrl=settings.SQS_URL, MaxNumberOfMessages=10, WaitTimeSeconds=0
        )

        messages = response.get("Messages", None)
        if not messages:
            self.stdout.write(self.style.WARNING("No messages"))
            return messages

        for message in response["Messages"]:
            self.stdout.write(
                self.style.SUCCESS("Processing message [%s]" % message["MessageId"])
            )
            task_sqs_handler(message)
            receipt_handle = message["ReceiptHandle"]
            client.delete_message(
                QueueUrl=settings.SQS_URL, ReceiptHandle=receipt_handle
            )
            self.stdout.write(
                self.style.SUCCESS("Message consumed [%s]" % message["MessageId"])
            )

        return messages
