from django.db import models
from django.utils import timezone


class Bet(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    value = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish_bet(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.value
