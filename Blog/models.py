from django.db import models
# import user model 
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	# define attributes :
	title = models.CharField(max_length=50)
	content = models.TextField()
	posted_at = models.DateTimeField(auto_now_add=True)
	# on_delete option manage if the user has been deleted :
	author = models.ForeignKey(User,on_delete=models.CASCADE)