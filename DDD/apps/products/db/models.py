a = 1
from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Products(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'products'