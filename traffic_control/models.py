from django.db import models
from django.contrib.auth.models import User


# Traffic Light Model
class TrafficLight(models.Model):
    intersection_name = models.CharField(max_length=200)
    green_light_duration = models.IntegerField(default=30)  # in seconds
    red_light_duration = models.IntegerField(default=30)
    traffic_density = models.IntegerField(default=0)  # vehicles per minute

    def __str__(self):
        return self.intersection_name


# User Registration Model
class UserRegistration(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)  # Example of an additional field


# Traffic Police Model
class TrafficPolice(models.Model):
    name = models.CharField(max_length=255)
    rank = models.CharField(max_length=100)
    badge_number = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='officer_photos/', blank=True, null=True)
    rating = models.IntegerField(default=0)  # Optional rating
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional location

    def __str__(self):
        return self.name


# Traffic Report Model
class TrafficReport(models.Model):
    road_name = models.CharField(max_length=255)
    delay = models.IntegerField()  # Delay in minutes
    distance = models.FloatField()
    status = models.CharField(max_length=100)  # e.g., "Heavy Traffic"
    assigned_officer = models.ForeignKey(TrafficPolice, on_delete=models.CASCADE)
    progress = models.CharField(max_length=255, default="Not Started")  # Progress of the assigned task
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Report for {self.road_name} by {self.assigned_officer.name}"


# Congested Road Model
class CongestedRoad(models.Model):
    road_name = models.CharField(max_length=255)
    congestion_level = models.CharField(max_length=50, choices=[
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ])
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)  # Optional

    def __str__(self):
        return self.road_name


# Report Model
class Report(models.Model):
    road = models.ForeignKey(CongestedRoad, on_delete=models.CASCADE, related_name="reports")
    sent_by = models.CharField(max_length=255)  # Traffic controller's name or ID
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()  # Additional notes for the traffic police

    def __str__(self):
        return f"Report for {self.road.road_name} by {self.sent_by}"


# Developer Model
class Developer(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


# Traffic Area Model
class TrafficArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
