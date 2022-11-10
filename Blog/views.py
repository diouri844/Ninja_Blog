from django.shortcuts import render
from django.http import HttpResponse
# define an context object to passe :
posts = [
	{'id':1, 'title':'Blog 1','author':'Chopen',"date":"10-10-2022"	},
	{'id':2, 'title':'Blog 2','author':'Ch_builder',"date":"9-10-2022"	},
	{'id':3, 'title':'Blog 3','author':'Chopen',"date":"1-9-2022"	},
	{'id':4, 'title':'Blog 4','author':'Chopen',"date":"10-10-2021"	}
]
# Create your views here.
def Blog_home(request):
	# rendder the home template : 2 arguments 
	# arg 1: request object 
	# arg 2: template path as string  
	# after define our post list pass it as an argument :
	context = { 'posts':posts }
	return render(request,'Blog/Home.html', context)

def Blog_about(request):
	return render(request,'Blog/About.html')