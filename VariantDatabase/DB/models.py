from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Testvariant(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)])
    proband = models.BooleanField(choices=((True,"Y"),(False,"N")), null=True)
    #affected_relatives = models.BooleanField(choices=((True,"Y"),(False,"N")), null=True)
    #stage = models.IntegerField(choices=((1,"1"),(2,"2"),(3,"3")), null=True)
    description = models.CharField(max_length=500, null=True, name='Description')
    sequencer = models.CharField(choices=(("HiSeq", "HiSeq"), ("MiSeq", "MiSeq")), max_length=20, null=True)
    gene = models.CharField(max_length=10, null=True)
    #chrm = models.CharField(null=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"),("X","X"),("Y","Y")), max_length=2)
    variant_cdna = models.CharField(max_length=200, null=True)
    variant_protein = models.CharField(max_length=200, null=True)
    variant_genome = models.CharField(blank=False, max_length=200, null=True)
    code_pathogenicity = models.CharField(blank=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5")), max_length=1)
    codes_evidence = models.CharField(max_length=200, blank=True)
    uploaded_time = models.DateTimeField(blank=True, null=True)
#todo: split the table into separate tables
    def __str__(self):
        return self.name
