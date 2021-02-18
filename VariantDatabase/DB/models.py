from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(null=False)
    name = models.CharField(max_length=200, name='name')
    age = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(120)], name='age')
    proband = models.BooleanField(choices=((True,"Y"),(False,"N")), null=True, name='proband', blank=True)
    affected_relatives = models.BooleanField(choices=((True,"Y"),(False,"N")), null=True, name='affected_relatives', blank=True)
    stage = models.IntegerField(choices=((1,"1"),(2,"2"),(3,"3")), null=True, name='stage')
    description = models.CharField(max_length=500, null=True, name='description')

    def __str__(self):
        return self.patient_id

class Testvariant(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    sequencer = models.CharField(choices=(("HiSeq", "HiSeq"), ("MiSeq", "MiSeq")), max_length=20, null=True, name='sequencer')
    gene = models.CharField(max_length=10, null=True, name='gene', default='BRCA1')
    chrm = models.CharField(null=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"),("X","X"),("Y","Y")), max_length=2, name='chrm')
    variant_cdna = models.CharField(max_length=200, null=True, name='variant_cdna')
    variant_protein = models.CharField(max_length=200, null=True, name='variant_protein')
    variant_genome = models.CharField(blank=False, max_length=200, null=True, name='variant_genome')

    def __str__(self):
        return self.variant_cdna
    # todo: either one of cDNA and genome coordinate is required input rather than both?

class Interpretation(models.Model):
    code_pathogenicity = models.CharField(blank=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5")), max_length=1, name="code_pathogenicity")
    codes_evidence = models.CharField(max_length=200, blank=True, name="codes_evidence")
    testvariant = models.ForeignKey(Testvariant, on_delete=models.CASCADE, null=True)
    #uploaded_time = models.DateTimeField(blank=True, null=True, name="uploaded_time")

    def __str__(self):
        return self.code_pathogenicity