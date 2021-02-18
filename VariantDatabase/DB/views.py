from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import InputForm
from .models import Patient_data, Variant_data

# Create your views here.
def Homepage(request):
    Variants = Variant_data.objects.all()
    return render(request, 'DB/homepage.html', {'Variants': Variants})

def Variantpage(request):
    Variants = Variant_data.objects.all()
    return render(request, 'DB/variantpage.html', {'Variants': Variants})


def Datainputpage(request):

    if request.method == 'POST':

        form = InputForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            proband = form.cleaned_data['proband']
            affected_relatives = form.cleaned_data['affected_relatives']
            stage = form.cleaned_data['stage']
            description = form.cleaned_data['description']
            sequencer = form.cleaned_data['sequencer']
            gene = form.cleaned_data['gene']
            chrm = form.cleaned_data['chrm']
            variant_cdna = form.cleaned_data['variant_cdna']
            variant_protein = form.cleaned_data['variant_protein']
            variant_genome = form.cleaned_data['variant_genome']
            code_pathogenicity = form.cleaned_data['code_pathogenicity']
            codes_evidence = form.cleaned_data['codes_evidence']
            uploaded_time = form.cleaned_data['uploaded_time']
            print(name)
            return HttpResponseRedirect('/None/')
    else:
       form = InputForm()

    return render(request, 'DB/datainputpage.html', {'form' : form})

def Bulkinputpage(request):



    return render(request, 'DB/bulkinputpage.html', {})
