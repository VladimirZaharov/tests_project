from django.contrib.auth.models import AbstractUser
from django.db import models

from tests.models import Test


class User(AbstractUser):
    current_test = models.JSONField(blank=True, null=True)


class UserStatistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)
    result = models.IntegerField(default=0)
