from django.contrib import admin

# Register your models here.
from .models import TrafficLight
from .models import TrafficPolice

admin.site.register(TrafficLight)
admin.site.register(TrafficPolice)