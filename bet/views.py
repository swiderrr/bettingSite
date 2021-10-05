from django.shortcuts import render, get_object_or_404, redirect
from .models import Bet, Person
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from .functions import covidCases, compareBets


def home_page(request):
    todaysDate = datetime.now().strftime("%d-%m-%Y")
    personObjs = Person.objects.all()
    currentTime = int(datetime.now().strftime("%H"))
    if request.user.is_authenticated:
        currentUser = request.user.username
        currentPersonObj = Person.objects.filter(personName=currentUser)
        person = currentPersonObj[0]
        covidsToday = covidCases()
        bestBet = compareBets(personObjs, covidsToday)
        if request.method == "POST":
            betValue = request.POST['typ']
            person.bet = betValue
            person.save()
            return render(request, 'bet/homepage.html', {
                'person': person,
                'personObjs': personObjs,
                'todaysDate': todaysDate,
                'currentTime': currentTime,
                'covidsToday': covidsToday,
                'bestBet': bestBet,
            })
        else:
            return render(request, 'bet/homepage.html', {
                'person': person,
                'personObjs': personObjs,
                'todaysDate': todaysDate,
                'currentTime': currentTime,
                'covidsToday': covidsToday,
                'bestBet': bestBet,
            })
    else:
        return render(request, 'bet/homepage.html',)


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
