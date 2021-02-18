import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import InputForm
from .models import Patient_data, Variant_data, Test_data, Interpretation_data
from django.shortcuts import render
from django.views.generic import ListView
from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML
from django.contrib.auth.models import User

# Create your views here.
def Homepage(request):

    Variants = Variant_data.objects.all()

    return render(request, 'DB/Homepage.html', {'Variants': Variants})

def Variantpage(request):
    Patients = Patient_data.objects.all()
    Variants = Variant_data.objects.all()
    return render(request, 'DB/variantpage.html', {'Patients': Patients})
    return render(request, 'DB/variantpage.html', {'Variants': Variants})


def Datainputpage(request):


    if request.method == 'POST':

        form = InputForm(request.POST)

        if form.is_valid():

            patient, creation = Patient_data.objects.get_or_create(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age'],
                proband = form.cleaned_data['proband'],
                stage = form.cleaned_data['stage'],
                description = form.cleaned_data['description']
            )

            variant, creation = Variant_data.objects.get_or_create(
                gene = form.cleaned_data['gene'],
                chrm = form.cleaned_data['chrm'],
                variant_cdna = form.cleaned_data['variant_cdna'],
                variant_protein = form.cleaned_data['variant_protein'],
                variant_genome = form.cleaned_data['variant_genome'])
                
                
            test, creation = Test_data.objects.get_or_create(
                patient_id = patient, 
                sequencer = form.cleaned_data['sequencer'],
                variant_id = variant,
                uploaded_time = datetime.datetime.now())
            
            interpretation, creation = Interpretation_data.objects.get_or_create(
                variant_id = variant,
                code_pathogenicity = form.cleaned_data['code_pathogenicity'],
                codes_evidence = form.cleaned_data['codes_evidence'],
                uploaded_time = datetime.datetime.now())

            #return HttpResponseRedirect('DB/datainputpage.html')
    else:
       form = InputForm()

    return render(request, 'DB/datainputpage.html', {'form' : form})

def Bulkinputpage(request):



    return render(request, 'DB/bulkinputpage.html', {})
