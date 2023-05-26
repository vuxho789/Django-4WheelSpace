from django.shortcuts import render, redirect
from .models import Team
from cars_app.models import Car
from django.contrib.auth.models import User
from django.contrib import messages
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_date')
    latest_cars = Car.objects.order_by('-created_date')[:6]

    make_search = Car.objects.values_list('make', flat=True).distinct().order_by('make')
    model_search = Car.objects.values_list('model', flat=True).distinct().order_by('model')
    year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
    state_search = Car.objects.values_list('state', flat=True).distinct().order_by('state')
    body_search = Car.objects.values_list('body_style', flat=True).distinct().order_by('body_style')

    data = {'teams': teams,
            'featured_cars': featured_cars,
            'latest_cars': latest_cars,
            'make_search': make_search,
            'model_search': model_search,
            'year_search': year_search,
            'state_search': state_search,
            'body_search': body_search,}
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {'teams': teams,}
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = '4WheelSpace - You have a new message'
        email_data = {'full_name': full_name, 'email': email, 'phone': phone,
                      'subject': subject, 'message': message}

        plain_body = render_to_string('emails/new_message.txt', {'contact': email_data})
        html_body = render_to_string('emails/new_message.html', {'contact': email_data})
        send_mail(email_subject, plain_body,
                  EMAIL_HOST_USER,
                  [admin_email],
                  html_message = html_body,
                  fail_silently=False,)
        
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    else:
        return render(request, 'pages/contact.html')
    
def health(request):
    return HttpResponse('Health check passed', status=200)
    
