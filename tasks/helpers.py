from django.utils import timezone

from .models import Task


def complete_task(task_uuid):
    try:
        task = Task.objects.get(uuid=task_uuid, completed_at=None)
    except Task.DoesNotExist:
        return

    task.completed_at = timezone.now()
    task.save()
