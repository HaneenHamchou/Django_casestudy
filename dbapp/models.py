from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create Corporation models to represent database tables .
class Corporations(models.Model):
	id = models.AutoField(null=False, primary_key=True)
	name = models.CharField(max_length = 100)
	address = models.TextField()
	url = models.URLField(null=True)
	#relationship between Corporation Model and User Model
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class User(AbstractUser):
    id = models.AutoField(null=False, primary_key=True)
    name = CharField(blank=True, max_length=255)


	def __str__(self):
		return self.name

