from django.db import models
from django.utils import timezone


class Visit(models.Model):
    time_stamp = models.DateTimeField(default=timezone.now)
    ip_address = models.CharField(max_length=20, null=True)
    url = models.CharField(max_length=200)
    url_name = models.CharField(max_length=50)
    app_name = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "visits"

    def __str__(self):
        return self.time_stamp.strftime("%m/%d/%Y, %H:%M:%S")
