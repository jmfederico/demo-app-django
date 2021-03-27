from django.db import models


class Task(models.Model):
    uuid = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
