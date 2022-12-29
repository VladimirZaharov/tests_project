from django.db import models


class Answer(models.Model):
    name = models.CharField(max_length=256, blank=True)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=256, blank=True)
    answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return self.name
