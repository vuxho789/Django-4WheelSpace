from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail', '__str__', 'role', 'created_date')
    list_display_links = ('id', '__str__')
    search_fields = ('first_name', 'last_name', 'role')
    list_filter = ('role',)
    
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius: 50px;" />')
    
    thumbnail.short_description = 'Photo'

admin.site.register(Team, TeamAdmin)