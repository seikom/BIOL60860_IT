import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
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
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        Variants = Variant_data.objects.filter(gene__icontains=search_term)
    else:
        Variants = Variant_data.objects.all()

    return render(request, 'DB/homepage.html', {'Variants' : Variants, 'search_term': search_term })

def Variantpage(request, variant_id):

    Variant = get_object_or_404(Variant_data, variant_id=variant_id)

    Tests = Test_data.objects.filter(variant_id__exact=variant_id)

    Interpretations = Interpretation_data.objects.filter(variant_id__exact=variant_id)

    context = {

    'Variant': Variant,
    'Tests' : Tests,
    'Interpretations' : Interpretations,
    }

    return render(request, 'DB/variantpage.html', context)


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
                variant_genome = form.cleaned_data['variant_genome']
            )


            test, creation = Test_data.objects.get_or_create(
                patient_id = patient,
                sequencer = form.cleaned_data['sequencer'],
                variant_id = variant,
                uploaded_time = datetime.datetime.now()
            )

            interpretation, creation = Interpretation_data.objects.get_or_create(
                variant_id = variant,
                code_pathogenicity = form.cleaned_data['code_pathogenicity'],
                codes_evidence = form.cleaned_data['codes_evidence'],
                uploaded_time = datetime.datetime.now()
            )

                # Need to make the page refresh or give some recognition its done something
                #return HttpResponseRedirect('DB/datainputpage.html')
    else:
       form = InputForm()

    return render(request, 'DB/datainputpage.html', {'form' : form})

def Bulkinputpage(request):



    return render(request, 'DB/bulkinputpage.html', {})


class SearchView(ListView):
    model = Variant_data
    template_name = 'homepage.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Variant_data.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result
