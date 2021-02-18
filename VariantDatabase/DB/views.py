from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Testvariant

# Create your views here.
def Homepage(request):
     return render(request, 'DB/homepage.html', {})

def Variantpage(request):
    Variants = Testvariant.objects.all()
    return render(request, 'DB/variantpage.html', {'Variants': Variants})
