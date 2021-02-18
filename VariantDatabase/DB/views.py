from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import InputForm
from .models import Patient_data, Variant_data
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def Homepage(request):

    Variants = Variant_data.objects.all()

    return render(request, 'DB/homepage.html', {'Variants': Variants})

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

            add_variant = Variant_data.objects.create(
                patient = patient,
                sequencer = form.cleaned_data['sequencer'],
                gene = form.cleaned_data['gene'],
                chrm = form.cleaned_data['chrm'],
                variant_cdna = form.cleaned_data['variant_cdna'],
                variant_protein = form.cleaned_data['variant_protein'],
                variant_genome = form.cleaned_data['variant_genome'],
                code_pathogenicity = form.cleaned_data['code_pathogenicity'],
                codes_evidence = form.cleaned_data['codes_evidence'])
                #uploaded_time = form.cleaned_data['uploaded_time'])

            #return HttpResponseRedirect('DB/datainputpage.html')
    else:
       form = InputForm()

    return render(request, 'DB/datainputpage.html', {'form' : form})

def Bulkinputpage(request):



    return render(request, 'DB/bulkinputpage.html', {})
