from django import forms
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class InputForm(forms.Form):

    name = forms.CharField(label='name', max_length=200)
    age = forms.IntegerField(label='age', validators=[MinValueValidator(0),MaxValueValidator(120)])
    proband = forms.BooleanField(label='proband')
    affected_relatives = forms.BooleanField(label='affected_relatives')
    stage = forms.ChoiceField(label='stage')
    description = forms.CharField(label='description', max_length=500)
    sequencer = forms.ChoiceField(label='sequencer', choices=[("HiSeq", "HiSeq"), ("MiSeq", "MiSeq")])
    gene = forms.CharField(label='gene', max_length=10)
    chrm = forms.ChoiceField(label='chrm', choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"),("X","X"),("Y","Y")])
    variant_cdna = forms.CharField(label='variant_cdna', max_length=200)
    variant_protein = forms.CharField(label='variant_protein', max_length=200)
    variant_genome = forms.CharField(label='variant_genome', max_length=200)
    code_pathogenicity = forms.ChoiceField(label="code_pathogenicity", choices=[("1","1"),("2","2"),("3","3"),("4","4"),("5","5")])
    codes_evidence = forms.CharField(label="codes_evidence", max_length=200)
    uploaded_time = forms.DateTimeField(label="uploaded_time")