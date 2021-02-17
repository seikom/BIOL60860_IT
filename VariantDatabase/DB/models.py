from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Testvariant(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    proband = models.BooleanField()
    #
    sequencer = models.CharField()
    variant_cdna = models.CharField()
    variant_protein = models.CharField()
    variant_genome = models.CharField(blank=False)
    code_pathogenicity = models.IntegerField(blank=True)
    codes_evidence = models.CharField(max_length=200, blank=True)
    uploaded_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
