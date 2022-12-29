from django.db import models

from questions.models import Question


class TestCategory(models.Model):
    name = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=256, blank=True)
    category = models.ForeignKey(TestCategory, on_delete=models.SET_NULL, null=True)
    questions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return self.name