from django.db import models

# Create Corporation models to represent database tables .
class Corporations(Model.models):
	name = models.CharField(max_lenght = 100)
	address = models.TextField()
	url = models.URLField(null=True)
	#relationship between Corporation Modela and User Model
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
        return self.name
