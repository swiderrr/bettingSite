import bs4, requests
from .models import Person


def covidCases():
    covidResponse=requests.get("https://koronawirusunas.pl/")
    soup = bs4.BeautifulSoup(covidResponse.text, features="lxml")
    covidCases = soup.select('span[title="Zakażeni"]')[0].getText().replace(' ', '')
    return covidCases

def compareBets(personList, covidsToday):
    absolute = 999999
    for iter, p in enumerate(personList):
        newAbsolute = abs(p.bet - int(covidsToday))
        if newAbsolute < absolute:
            absolute = newAbsolute
            closestBet = p.bet
    return closestBet


def givePoint():
    winner = Person.objects.filter(bet=compareBets(Person.objects.all(), covidCases()))[0]
    winner.points = winner.points + 1
    print(winner.points)
    winner.save()
    print("Sprawdzanie")
    return