from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        car_name = request.POST['car_name']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        customer_need = request.POST['customer_need']

        # Check if the user is logged in
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car.')
                return redirect(f'/cars/{car_id}')
        
        # Add the inquiry message to the database
        contact = Contact(first_name=first_name, last_name=last_name, user_id=user_id,
                          car_id=car_id, car_name=car_name, city=city, state=state,
                          email=email, phone=phone, message=message, customer_need=customer_need)
        contact.save()

        # Send a simple email to admin
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = '4WheelSpace - New Car Inquiry'
        email_body = f'You have a new inquiry for the car {car_name}. Please login to the admin panel for more info.'
        send_mail(email_subject, email_body,
                  EMAIL_HOST_USER,
                  [admin_email],
                  fail_silently=False,)
                
        # Send a message in the frontend
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect(f'/cars/{car_id}')