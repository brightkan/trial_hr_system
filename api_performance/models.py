from django.db import models
from django.utils import timezone


class APIRequestLog(models.Model):
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    status_code = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)
    success = models.BooleanField()

    def __str__(self):
        return f'{self.method} {self.endpoint} - {self.status_code} - {"Success" if self.success else "Failed"}'
