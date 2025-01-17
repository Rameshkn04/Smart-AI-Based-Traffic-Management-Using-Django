# Generated by Django 5.1.3 on 2024-12-17 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trafficpolice',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='trafficpolice',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='officers_photos/'),
        ),
        migrations.AddField(
            model_name='trafficpolice',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
