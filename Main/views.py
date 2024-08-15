from django.shortcuts import render
from . models import *
from . serializers import *

# Create your views here.

def Home(request):
    return render(request, 'home.html')


def CompanyViews(request):
    return render(request, 'company.html')