from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', 'car_name', 'colour', 'body_style', 'transmission', 'fuel_type', 'state', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_name')
    list_editable = ('is_featured',)
    search_fields = ('car_name', 'body_style', 'transmission', 'fuel_type', 'state')
    list_filter = ('model', 'body_style', 'transmission', 'fuel_type', 'state')

    def thumbnail(self, object):
        return format_html(f'<img src="{object.car_photo.url}" width="40" style="border-radius: 50px;" />')
    
    thumbnail.short_description = 'Car Image'

admin.site.register(Car, CarAdmin)