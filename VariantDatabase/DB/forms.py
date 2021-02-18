from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class InputForm(forms.Form):

    name = forms.CharField(label='Patient name', max_length=200)
    age = forms.IntegerField(label='Patient age', validators=[MinValueValidator(0),MaxValueValidator(120)])
    proband = forms.BooleanField(label='Proband status')
    affected_relatives = forms.BooleanField(label='Affected Relatives?')
    stage = forms.ChoiceField(label='Stage', choices=[("Not cancer", "Not cancer"),("1","1"),("2","2"),("3","3")])
    description = forms.CharField(label='Description', max_length=500)
    sequencer = forms.ChoiceField(label='Sequencer', choices=[("HiSeq", "HiSeq"), ("MiSeq", "MiSeq")])
    gene = forms.CharField(label='Gene', max_length=10)
    chrm = forms.ChoiceField(label='Chromosome', choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"),("X","X"),("Y","Y")])
    variant_cdna = forms.CharField(label='Variant cDNA', max_length=200)
    variant_protein = forms.CharField(label='Variant Protein', max_length=200)
    variant_genome = forms.CharField(label='Variant genome reference', max_length=200)
    code_pathogenicity = forms.ChoiceField(label="Pathogenicity Code", choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")])
    codes_evidence = forms.CharField(label="ACGM evidence codes", max_length=200)