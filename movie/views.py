import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def movie(request):
    return HttpResponse('<h1>Voy pa la ICPC carreado</h1>')