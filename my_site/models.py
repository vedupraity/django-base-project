from datetime import datetime

from django.db import models

from core.models import TimestampedModel, UserOwnedModel
from .querysets import TodoTaskQueryset


class TodoTask(TimestampedModel, UserOwnedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    due_by = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    objects = TodoTaskQueryset.as_manager()

    @property
    def is_due(self):
        return not self.is_completed and (
                self.due_by is None or datetime.now() < self.due_by
        )

    @property
    def is_overdue(self):
        return not self.is_completed and datetime.now() > self.due_by
