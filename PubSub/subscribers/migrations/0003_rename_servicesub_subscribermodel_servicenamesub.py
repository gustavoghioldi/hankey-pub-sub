# Generated by Django 4.1.3 on 2022-11-29 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_remove_subscribermodel_servicepub_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribermodel',
            old_name='serviceSub',
            new_name='serviceNameSub',
        ),
    ]