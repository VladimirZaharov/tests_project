from django.db import models

from tests.models import Test


class Question(models.Model):
    name = models.CharField(max_length=256, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField(max_length=256, blank=True)
    is_right = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

