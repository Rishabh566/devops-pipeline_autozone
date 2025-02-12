from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
	first_name= models.CharField(max_length=200)
	last_name= models.CharField(max_length=200)
	car_id = models.IntegerField()
	customer_needs= models.CharField(max_length=200)
	car_title= models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	country = models.CharField(default='Ireland', max_length=100)
	email=models.EmailField(max_length=200)
	phone=models.CharField(max_length=200)
	message=models.TextField(blank=True)
	user_id=models.IntegerField(blank=True)
	created_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.email

