from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages


# Home
def home(request):
    return render(request, 'crud_app/home.html')


# Register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, 'crud_app/register.html', {'form': form})


# Login
def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                auth_login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")

    return render(request, 'crud_app/login.html', {'form': form})


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    return render(request, "crud_app/dashboard.html", {'records': records})


# Create Record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect("dashboard")

    return render(request, 'crud_app/create_record.html', {'form': form})


# Update Record
@login_required(login_url='login')
def update_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect("dashboard")

    return render(request, 'crud_app/update-record.html', {'form': form})


# View Single Record
@login_required(login_url='login')
def singular_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    return render(request, 'crud_app/view_record.html', {'record': record})


# Delete Record
@login_required(login_url='login')
def delete_record(request, pk):
    record = get_object_or_404(Record, id=pk)
    record.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect("dashboard")


# Logout
def logout(request):
    auth_logout(request)
    return redirect("login")