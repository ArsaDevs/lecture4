# Generated by Django 3.1 on 2020-08-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20200814_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=15)),
                ('last', models.CharField(max_length=15)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
