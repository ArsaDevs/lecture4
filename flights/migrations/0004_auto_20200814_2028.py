# Generated by Django 3.1 on 2020-08-14 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_pax'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pax',
            new_name='Passenger',
        ),
    ]