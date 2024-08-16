from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import viewsets


# Create your views here.

def Home(request):
    return render(request, 'home.html')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer