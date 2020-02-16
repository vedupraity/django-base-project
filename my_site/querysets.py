from datetime import datetime

from django.db.models import Q, QuerySet


class TodoTaskQueryset(QuerySet):
    def active_tasks(self):
        return self.filter(
            Q(is_completed=False),
            Q(due_by=None) | Q(due_by__gte=datetime.now())
        )

    def get_overdue_tasks(self):
        return self.filter(
            Q(is_completed=False),
            Q(due_by__lt=datetime.now())
        )

    def get_completed_tasks(self):
        return self.filter(is_completed=True)
