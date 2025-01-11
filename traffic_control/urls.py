from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home page
     path('login/', views.custom_login, name='login'),  # Login page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('logout/', LogoutView.as_view(), name='logout'), # Logout view   
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'
    ), name='password_reset'),  # Password reset
    path('signup/', views.signup, name='signup'),  # Define the signup URL
    path('login/register/', views.register, name='register'),  # Registration page
    path('traffic_control/', views.traffic_control, name='traffic_control'),
    path('TafficMap/', views.TrafficMap, name='TrafficMap'),
    path('reports/', views.reports, name='reports'),
    path('user-management/', views.user_management, name='user_management'),
    path('traffic-police/', views.traffic_police_list, name='traffic_police_list'),
    path('notifications/', views.notifications, name='notifications'),
    path('analytics/', views.analytics, name='analytics'),
    path('help-support/', views.help_support, name='help_support'),
    path('profile/', views.profile, name='profile'),
    # URL to show the report submission form
     path('reports/traffic_police/', views.traffic_police, name='traffic_police'),
    # You may also have this:
    path('reports/submit_report/', views.submit_report, name='submit_report'),
     path('traffic-info/', views.traffic_info, name='traffic_info'),
    path('reports/', views.reports, name='reports'),
    path('add-traffic-police/', views.add_traffic_police, name='add_traffic_police'),
   path('traffic-police/', views.traffic_police_list, name='traffic-police-list'),
    path('traffic-police/<int:id>/', views.traffic_police_detail, name='traffic_police_detail'),  # Add this line
    path('traffic-police/delete/<int:id>/', views.traffic_police_delete, name='traffic_police_delete'),  # Add this line
    path('assistant/', views.assistant, name='assistant'),
    path('get-response/', views.get_response, name='get_response'),  # For handling user input
     path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('login/forgot-password/', views.forgot_password, name='forgot_password'),
     path('traffic-police-list/', views.traffic_police_list, name='traffic_police_list'),
    path('traffic-police/<int:id>/', views.traffic_police_detail, name='traffic_police_detail'),
    path('delete-traffic-police/<int:id>/', views.traffic_police_delete, name='traffic_police_delete'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
