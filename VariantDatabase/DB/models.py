from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Testvariant(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=3, )
    proband = models.BooleanField(blank=True)
    affected_relatives = models.BooleanField(blank=True)
    stage = models.IntegerField(choices=(("1","1"),("2","2"),("3","3")))
    description = models.CharField(max_length=500)
    sequencer = models.CharField(cohices=(("HiSeq", "HiSeq"), ("MiSeq", "MiSeq")))
    gene = models.CharField(max_length=10, blank=True)
    variant_cdna = models.CharField(max_length=200)
    variant_protein = models.CharField(max_length=200)
    variant_genome = models.CharField(blank=False, max_length=200)
    code_pathogenicity = models.CharField(blank=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5")), max_length=1)
    codes_evidence = models.CharField(max_length=200, blank=True)
    uploaded_time = models.DateTimeField(blank=True, null=True)
#todo: split the table into separate tables
    def __str__(self):
        return self.name
