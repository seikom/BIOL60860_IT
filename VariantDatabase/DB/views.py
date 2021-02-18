from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import InputForm
from .models import Testvariant

# Create your views here.
def Homepage(request):
     return render(request, 'DB/homepage.html', {})

def Variantpage(request):
    Variants = Testvariant.objects.all()
    return render(request, 'DB/variantpage.html', {'Variants': Variants})


def Datainputpage(request):

    #if request.method == 'POST':

        #form = InputForm(request.POST)

        #if form.is_valid():
            #pass
            #return HttpResponseRedirect('/None/')
        #else:
           #form = InputForm()

    return render(request, 'DB/datainputpage.html', {})

def Bulkinputpage(request):



    return render(request, 'DB/bulkinputpage.html', {})
