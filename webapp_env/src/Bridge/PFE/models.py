from django.db import models

# Create your models here.
class PFE(models.Model):
	name 			= models.CharField(max_length=30)
	email			= models.EmailField()
	title			= models.CharField(max_length=100)
	description 	= models.TextField()
	document 		= models.FileField()

	
