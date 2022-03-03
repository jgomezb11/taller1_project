import re
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import re_path

# Create your views here.

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')
    
def movie(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'movie.html', {'name':'Julian', 'searchTerm':searchTerm})