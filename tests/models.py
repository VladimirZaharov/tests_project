from django.db import models


class TestCategory(models.Model):
    name = models.CharField(max_length=256, blank=True)


class Test(models.Model):
    name = models.CharField(max_length=256, blank=True)
    category = models.ForeignKey(TestCategory, on_delete=models.SET_NULL)
