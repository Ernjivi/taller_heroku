from django.db import models
from django.conf import settings


class BMI(models.Model):
    """
    Hold bmi records of users.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()

    def __str__(self):
        return self.user.username

