from django.shortcuts import render
from django.http import HttpResponse

# import User model : 
from django.contrib.auth.models import User

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

def Blog_login(request):
	if request.method == "POST":
		print("sending data form :     \n")
		user_name =request.POST.get('userName')
		user_email =request.POST.get('userEmail')
		user_password =request.POST.get('userPassword')
		print(user_name,user_email,user_password)
		response_fetch = list(User.objects.all())
		print("\n response fetch :   ",
			response_fetch[0].username,
			response_fetch[0].email,
			)
	return render(request,'Blog/Login.html')

def Blog_register(request):
	return render(request,'Blog/Register.html')