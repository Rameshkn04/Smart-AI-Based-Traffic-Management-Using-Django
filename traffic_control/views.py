from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
import cv2
import os
from .models import TrafficReport, TrafficPolice
from traffic_control.models import TrafficPolice
from .models import CongestedRoad, Report


def home(request):
    return render(request, 'traffic_control/home.html')  # Ensure this matches your template location

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace with your dashboard URL
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'traffic_control/login.html')

# The dashboard view
@login_required
def dashboard(request):
    return render(request, 'traffic_control/dashboard.html') 
def signup(request):
    # Your signup logic here
    return render(request, 'traffic_control/signup.html')  # Assuming you have a signup template
def register(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate passwords
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use.')
            return redirect('register')

        # Create and save user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Redirect to login with success message
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login')

    return render(request, 'traffic_control/register.html')
def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
def traffic_control(request):
    video_url = None
    if request.method == "POST" and request.FILES['video']:
        video = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(video.name, video)
        video_url = fs.url(filename)
        # Optional: Process video here using OpenCV
        cap = cv2.VideoCapture(fs.path(filename))
        # Real-time processing logic (e.g., detection)
        cap.release()

    return render(request, 'traffic_control/traffic_control.html', {'video_url': video_url}) # Create a profile.html template for the profile page
def TrafficMap(request):
    return render(request, 'traffic_control/TrafficMap.html') 
def reports(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'traffic_control/reports.html', {'reports': reports})

def user_management(request):
    return render(request, 'traffic_control/add_traffic_police.html')
def notifications(request):
    return render(request, 'traffic_control/notifications.html')
def analytics(request):
    return render(request, 'traffic_control/analytics.html')
from django.shortcuts import render
from .models import TrafficPolice, Developer  # Assuming Developer is a model

def help_support(request):
    # Fetch data from database
    police_contacts = TrafficPolice.objects.all()
    developer_contacts = Developer.objects.all()
    
    return render(request, 'traffic_control/help_support.html', {
        'police_contacts': police_contacts,
        'developer_contacts': developer_contacts,
    })
     
def profile(request):
    return render(request, 'traffic_control/developer.html') 

# View for displaying the report submission form
def submit_report(request):
    if request.method == 'POST':
        # Collecting the data from the form
        road_name = request.POST.get('road-name')
        delay = request.POST.get('delay')
        distance = request.POST.get('distance')
        status = request.POST.get('status')
        officer = request.POST.get('officer')
        location = request.POST.get('location')

        # Save the data to the database (creating a TrafficReport object)
        report = TrafficReport(
            road_name=road_name,
            delay=delay,
            distance=distance,
            status=status,
            officer=officer,
            location=location
        )
        report.save()

        # Show a success message and redirect to the traffic police page
        messages.success(request, 'Traffic report submitted successfully!')
        return redirect('traffic_police')

    return render(request, 'traffic_control/submit_report.html')


def traffic_police(request):    # Fetch all traffic police officers
    police_officers = TrafficPolice.objects.all()

    # Fetch all traffic reports for assigned officers
    reports = []
    for officer in police_officers:
        assigned_reports = officer.reports.all()  # All reports assigned to this officer
        reports.append((officer, assigned_reports))

    return render(request, 'traffic_control/traffic_police.html')


from django.shortcuts import render, redirect
from .models import CongestedRoad, Report
def traffic_info(request):
    congested_roads = CongestedRoad.objects.all().order_by('-updated_at')

    if request.method == "POST":
        road_id = request.POST.get('road_id')
        message = request.POST.get('message')
        sent_by = request.POST.get('sent_by', 'Anonymous')  # Default sender

        try:
            road = get_object_or_404(CongestedRoad, id=road_id)
            Report.objects.create(road=road, message=message, sent_by=sent_by)
            messages.success(request, "Report submitted successfully!")
        except CongestedRoad.DoesNotExist:
            messages.error(request, "Road not found!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

        return redirect('traffic_info')  # Redirect after submission

    return render(request, 'traffic_control/trafficinfo.html', {'congested_roads': congested_roads})

from django.shortcuts import render, redirect
from .models import TrafficPolice

def add_traffic_police(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rank = request.POST.get('rank')
        badge_number = request.POST.get('badge_number')
        contact_number = request.POST.get('contact_number')
        photo = request.FILES.get('image')  # Handle uploaded file

        # Save the data to the database
        TrafficPolice.objects.create(
            name=name,
            rank=rank,
            badge_number=badge_number,
            contact_number=contact_number,
            photo=photo,
        )

        # Redirect to the list view
        return redirect('traffic_police_list')

    # Render the add form template
    return render(request, 'traffic_control/add_traffic_police.html')


from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import TrafficPolice

def traffic_police_list(request):
    officers = TrafficPolice.objects.all()  # Fetch all officers from the database

    # Optional: Add Pagination
    paginator = Paginator(officers, 6)  # Show 6 officers per page
    page_number = request.GET.get('page')
    police = paginator.get_page(page_number)

    return render(request, 'traffic_control/traffic_police_list.html', {'police': police})


def traffic_police_detail(request, id):
    officer = get_object_or_404(TrafficPolice, id=id)
    return render(request, 'traffic_control/traffic_police_detail.html', {'officer': officer})

def traffic_police_delete(request, id):
    officer = get_object_or_404(TrafficPolice, id=id)
    if request.method == 'POST':  # Ensure deletion only occurs on POST request
        officer.delete()
        return redirect('traffic_police_list')
    return render(request, 'traffic_control/confirm_delete.html', {'officer': officer})


from django.shortcuts import render
from django.http import JsonResponse
from .models import TrafficPolice

def assistant(request):
    return render(request, 'traffic_control/assistant.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()
        response = "Sorry, I couldn't understand your request."
        
        # Parse for 'call [location] traffic police'
        if 'call' in user_input and 'traffic police' in user_input:
            # Extract location
            words = user_input.split()
            location = words[words.index('call') + 1] if len(words) > words.index('call') + 1 else None
            
            # Query database for the location
            if location:
                try:
                    officer = TrafficPolice.objects.get(location__icontains=location)
                    response = f"Calling {officer.name} ({officer.rank}) at {officer.contact_number}."
                except TrafficPolice.DoesNotExist:
                    response = f"No traffic police found for location: {location}."
        
        return JsonResponse({'response': response})
from django.shortcuts import redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page

#forgot password
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ForgotPasswordForm, ResetPasswordForm

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(str(user.pk).encode())

                reset_link = f'http://127.0.0.1:8000/reset-password/{uid}/{token}/'
                send_mail(
                    'Password Reset Request',
                    f'Click on the link to reset your password: {reset_link}',
                    'from@example.com',
                    [email],
                )

                messages.success(request, 'Password reset link has been sent to your email address.')
            except User.DoesNotExist:
                messages.error(request, 'No user found with that email address.')

            return redirect('forgot_password')  # Redirect to the same page

    else:
        form = ForgotPasswordForm()

    return render(request, 'traffic_control/forgot_password.html', {'form': form})

def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                messages.success(request, 'Your password has been reset successfully.')
                return redirect('login')
        else:
            form = ResetPasswordForm()

        return render(request, 'traffic_control/reset_password.html', {'form': form})
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('forgot_password')

from django.shortcuts import render, redirect
from .models import TrafficArea, TrafficPolice

def reports_view(request):
    traffic_areas = TrafficArea.objects.all()
    officers = TrafficPolice.objects.filter(assigned_area__isnull=True)  # Only unassigned officers

    if request.method == "POST":
        area_id = request.POST.get('area_id')
        officer_id = request.POST.get('officer_id')

        # Assign the officer to the traffic area
        area = TrafficArea.objects.get(id=area_id)
        officer = TrafficPolice.objects.get(id=officer_id)

        officer.assigned_area = area
        area.status = "Assigned"

        officer.save()
        area.save()

        return redirect('reports')  # Reload page

    return render(request, 'reports.html', {'traffic_areas': traffic_areas, 'officers': officers})


