from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentUserSerializer, AdminUserSerializer
from .models import StudentUser, AdminUser

# Create your views here.
def index(request):
    return render(request, "admin_index.html")
def dashboard(request):
    return render(request, "dashboard.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            if user_type == 'student':
                return redirect('student_dashboard')
            elif user_type == 'admin':
                return redirect('admin_dashboard')
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'Admin_login.html', {'error_message': error_message})

    return render(request, 'Admin_login.html')


@api_view(['GET', 'POST'])  # Allow both GET and POST methods
def register_view(request):
    if request.method == 'POST':
        user_type = request.data.get('user_type')

        if user_type == 'student':
            serializer = StudentUserSerializer(data=request.data)
        elif user_type == 'admin':
            serializer = AdminUserSerializer(data=request.data)
        else:
            return Response({'error': 'Invalid user type'}, status=400)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    else:
        # Display the registration form for GET requests
        return render(request, 'register.html')

