# Generated by Django 4.1.3 on 2022-11-29 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0003_rename_servicesub_subscribermodel_servicenamesub'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribermodel',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='subscribermodel',
            name='webhook',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
