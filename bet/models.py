from django.db import models
from django.utils import timezone


class Bet(models.Model):
    author = models.CharField(max_length=30)
    value = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish_bet(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.value

class Person(models.Model):
    personName = models.CharField(max_length=30)
    points = models.IntegerField(default=0)
    bet = models.IntegerField(default=0)

    def my_score(self):
        return self.points

    def my_bet(self):
        return self.bet

    def __str__(self):
        return self.personName