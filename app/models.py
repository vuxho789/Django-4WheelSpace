from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100)
    instagram_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
