import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def movie(request):
    return render(request, 'movie.html', {'name':'Julian'})