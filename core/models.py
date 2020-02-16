from django.db import models
from django.contrib.auth.models import User


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)


class UserOwnedModel(models.Model):
    class Meta:
        abstract = True

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
