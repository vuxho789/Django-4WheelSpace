from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

#----- Global Variables -----#
# Get a list of unique values for each search criteria
make_search = Car.objects.values_list('make', flat=True).distinct().order_by('make')
model_search = Car.objects.values_list('model', flat=True).distinct().order_by('model')
year_search = Car.objects.values_list('year', flat=True).distinct().order_by('year')
state_search = Car.objects.values_list('state', flat=True).distinct().order_by('state')
body_search = Car.objects.values_list('body_style', flat=True).distinct().order_by('body_style')

#----- Create your views here -----#
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    data = {'cars': paged_cars,
            # Values for search criteria are from global variables
            'make_search': make_search,
            'model_search': model_search,
            'year_search': year_search,
            'state_search': state_search,
            'body_search': body_search,}
    return render(request, 'cars/cars.html', data)


def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {'single_car': single_car,}
    return render(request, 'cars/car_details.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')

    # Make sure min_price and max_price are always included in the request
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    cars = cars.filter(price__gte=min_price, price__lte=max_price)

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'make' in request.GET:
        make = request.GET['make']
        if make:
            cars = cars.filter(make__iexact=make)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            cars = cars.filter(state__iexact=state)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
             
    data = {'cars': cars,
            # Values for search criteria are from global variables
            'make_search': make_search,
            'model_search': model_search,
            'year_search': year_search,
            'state_search': state_search,
            'body_search': body_search,}
    return render(request, 'cars/search.html', data)
