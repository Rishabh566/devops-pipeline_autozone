from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

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

		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
			if has_contacted:
				messages.error(request, 'You have already made an enquiry about this car, Please wait until we get back to you.')
				return redirect('/cars/'+car_id)

		contact = Contact(car_id=car_id, user_id=user_id, car_title=car_title, 
			first_name=first_name, last_name=last_name, customer_needs=customer_needs, city=city, 
			country=country, email=email, phone=phone, message=message)
		
		admin_info = User.objects.get(is_superuser=True)
		admin_email = admin_info.email
		
		#send_mail(
		  #  "New Car Inquiry",
		  #  "You have new Inquiry for the car" + car_title + ". Please login to Admin Panel for the new information",
		  #  "x21171203@student.ncirl.ie",
		  #  [admin_email],
		  #  fail_silently=True,
		#)
		contact.save()
		messages.success(request, "ThanKs for your Enquiry, we will contact you")
		return redirect('/cars/'+car_id)