from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

AU_states = (('NSW', 'New South Wales'),
             ('VIC', 'Victoria'),
             ('QLD', 'Queensland'),
             ('WA', 'Western Australia'),
             ('SA', 'South Australia'),
             ('TAS', 'Tasmania'),
             ('ACT', 'Australian Capital Territory'),
             ('NT', 'Northern Territory'),)

year_choices = []
for year in range(2000, (datetime.now().year+1)):
    year_choices.append((year, year))

features_choices = (('Cruise Control', 'Cruise Control'),
                    ('Audio Interface', 'Audio Interface'),
                    ('Airbags', 'Airbags'),
                    ('Air Conditioning', 'Air Conditioning'),
                    ('Seat Heating', 'Seat Heating'),
                    ('Alarm System', 'Alarm System'),
                    ('ParkAssist', 'ParkAssist'),
                    ('Power Steering', 'Power Steering'),
                    ('Reversing Camera', 'Reversing Camera'),
                    ('Direct Fuel Injection', 'Direct Fuel Injection'),
                    ('Auto Start/Stop', 'Auto Start/Stop'),
                    ('Wind Deflector', 'Wind Deflector'),
                    ('Bluetooth Handset', 'Bluetooth Handset'),)

door_choices = (('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5'),
                ('6', '6'),)

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=AU_states, max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choices, default=datetime.now().year)
    colour = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name='Price (AUD)')
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    kilometres = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    fuel_consumption = models.FloatField(verbose_name='Fuel Consumption (L/100km)')
    registration_plate = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_name