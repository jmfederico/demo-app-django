from uuid import uuid4

import boto3
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect

from .models import Task

client = boto3.client("sqs")


@csrf_protect
def tasks_view(request: HttpRequest):
    if request.method == "POST":
        if "clear" in request.POST:
            Task.objects.all().delete()
            return redirect(request.path_info)

        task = Task.objects.create(uuid=uuid4())

        if settings.SQS_URL:
            client.send_message(
                QueueUrl=settings.SQS_URL,
                DelaySeconds=10,
                MessageBody=str(task.uuid),
            )

        return redirect(request.path_info)

    return HttpResponse(
        render_to_string(
            "tasks/tasks.html",
            {"tasks": Task.objects.order_by("-created_at").all()},
            request,
        )
    )
