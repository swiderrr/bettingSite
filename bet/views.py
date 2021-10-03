from django.shortcuts import render, get_object_or_404, redirect
from .models import Bet, Person
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home_page(request):
    if request.user.is_authenticated:
        currentUser = request.user.username
        persons = Person.objects.filter(personName=currentUser)
        person = persons[0]
        return render(request, 'bet/homepage.html', {'person': person})
    else:
        return render(request, 'bet/homepage.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        userAuth = authenticate(request, username=username, password=password)
        if userAuth is not None:
            login(request, userAuth)
            return redirect('home_page')
        else:
            messages.success(request, ("Wystąpił błąd podczas logowania, spróbuj ponownie."))
            return redirect('login_user')
    else:
        return render(request, 'bet/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany")
    return redirect('home_page')