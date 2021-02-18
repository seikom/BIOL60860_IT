from django import forms

class InputForm(forms.Form):

    name = forms.CharField(label='name', max_length=200)
    age = forms.PositiveIntegerField(label='age', validators=[MinValueValidator(0),MaxValueValidator(120)])
    proband = forms.BooleanField(label='proband', choices=((True,"Y"),(False,"N")), null=True)
    affected_relatives = forms.BooleanField(label='affected_relatives', choices=((True,"Y"),(False,"N")), null=True)
    stage = forms.IntegerField(label='stage', choices=((1,"1"),(2,"2"),(3,"3")), null=True)
    description = forms.CharField(label='description', max_length=500, null=True)
    sequencer = forms.CharField(label='sequencer', choices=(("HiSeq", "HiSeq"), ("MiSeq", "MiSeq")), max_length=20, null=True)
    gene = forms.CharField(label='gene', max_length=10, null=True)
    chrm = forms.CharField(label='chrm', null=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),("12","12"),("13","13"),("14","14"),("15","15"),("16","16"),("17","17"),("18","18"),("19","19"),("20","20"),("21","21"),("22","22"),("X","X"),("Y","Y")), max_length=2)
    variant_cdna = forms.CharField(label='variant_cdna', max_length=200, null=True)
    variant_protein = forms.CharField(label='variant_protein', max_length=200, null=True)
    variant_genome = forms.CharField(label='variant_genome', blank=False, max_length=200, null=True)
    code_pathogenicity = forms.CharField(label="code_pathogenicity", blank=True, choices=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5")), max_length=1)
    codes_evidence = forms.CharField(label="codes_evidence", max_length=200, blank=True)
    uploaded_time = forms.DateTimeField(label="uploaded_time", blank=True, null=True)

