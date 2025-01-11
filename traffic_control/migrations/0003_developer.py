# Generated by Django 5.1.3 on 2024-12-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_control', '0002_trafficpolice_location_trafficpolice_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=15)),
            ],
        ),
    ]