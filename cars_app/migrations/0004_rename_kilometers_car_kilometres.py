# Generated by Django 3.2 on 2023-05-18 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_app', '0003_auto_20230519_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='kilometers',
            new_name='kilometres',
        ),
    ]
