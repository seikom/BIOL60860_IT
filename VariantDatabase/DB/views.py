from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import Testvariant

# Create your views here.

def Test(request):

    """displays test result
    """

    test = Testvariant.objects.all()

    return (request, 'DB/main.html', {test : 'test'})




def Get_variant(request):

    """Gets a specific variants according to the ID
    """

    return None


