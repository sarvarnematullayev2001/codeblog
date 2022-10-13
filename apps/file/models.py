# Python
import uuid
import datetime

# Django
from django.db import models

# Project
from core.base_model import BaseModel


def upload(instance, filename):
    today = datetime.datetime.now()
    file_format = filename.split('.')[-1]
    return f"{today.year}/{today.month}/{today.day}/{uuid.uuid4()}.{file_format}"


class File(BaseModel):
    file = models.FileField(upload_to=upload)
    format = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    ordering = models.IntegerField(default=1)
    
    def save(self, force_insert=False, force_update=False, using=None,
            update_fields=None):
        self.format = self.file.name.split('.')[-1]
        self.name = self.file.name if not self.name else self.name
        return super(File, self).save()