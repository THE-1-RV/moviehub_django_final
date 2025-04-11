from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Login, Search
from .forms import SignupForm, LoginForm, DeleteUserForm
from django.utils.timezone import now

def index(request):
    return render(request, "accounts/index.html")

def home(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] != data['cnf_password']:
                messages.error(request, "Password and Confirm Password should be same")
                return redirect('home')
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, "accounts/home.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Login.objects.filter(email=email, password=password).first()
            if user:
                messages.success(request, "Login Successful")
                return redirect('index')
            else:
                messages.error(request, "Invalid email or password")
                return redirect('log')
    else:
        form = LoginForm()
    return render(request, "accounts/log.html", {"form": form})

def deluser(request):
    if request.method == "POST":
        form = DeleteUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Login.objects.filter(email=email, password=password).first()
            if user:
                user.delete()
                messages.success(request, "Account deleted successfully")
                return redirect('index')
            else:
                messages.error(request, "Email or password do not match")
                return redirect('deluser')
    else:
        form = DeleteUserForm()
    return render(request, "accounts/deluser.html", {"form": form})

def history(request):
    if request.method == "POST":
        movie = request.POST.get("movie")
        if movie:
            Search.objects.create(movie=movie)
            messages.success(request, "Search Successful")
    allSearch = Search.objects.all()
    return render(request, "accounts/history.html", {"allSearch": allSearch})

def delete(request, sno):
    entry = Search.objects.filter(sno=sno).first()
    if entry:
        entry.delete()
        messages.success(request, "Record deleted successfully")
    return redirect("history")
