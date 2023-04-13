from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def inquiry(request):
	if request.method == 'POST':
		car_id = request.POST['car_id']
		car_title = request.POST['car_title']
		user_id = request.POST['user_id']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		customer_needs = request.POST['customer_needs']
		city = request.POST['city']
		country = request.POST['country']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']

		contact = Contact(car_id=car_id, user_id=user_id, car_title=car_title, 
			first_name=first_name, last_name=last_name, customer_needs=customer_needs, city=city, 
			country=country, email=email, phone=phone, message=message)
		contact.save()
		messages.success(request, "ThanKs for your Enquiry, we will contact you")
		return redirect('/cars/'+car_id)