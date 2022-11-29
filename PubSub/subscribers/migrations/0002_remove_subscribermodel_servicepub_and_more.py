# Generated by Django 4.1.3 on 2022-11-29 21:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribermodel',
            name='servicePub',
        ),
        migrations.AddField(
            model_name='subscribermodel',
            name='servicePub',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
