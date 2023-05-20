from django.shortcuts import render
from .models import Team
from cars_app.models import Car

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
    return render(request, 'pages/contact.html')