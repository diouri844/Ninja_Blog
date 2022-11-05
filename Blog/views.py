from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Blog_home(request):
	return HttpResponse('<h1> Blog List b</h1>')