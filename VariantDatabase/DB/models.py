from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Testvariant(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    proband = models.BooleanField()
    uploaded_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
