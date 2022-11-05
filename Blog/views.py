from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Blog_home(request):
	# rendder the home template : 2 arguments 
	# arg 1: request object 
	# arg 2: template path as string  
	return render(request,'Blog/Home.html')

def Blog_about(request):
	return render(request,'Blog/About.html')