from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return super().get_queryset().filter(deleted_at=None)
        return super().get_queryset()
