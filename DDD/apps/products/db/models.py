from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class Products(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    description = models.TextField()

    rating = models.SmallIntegerField(
        validators=[MaxValueValidator(5)],
        null=True,
        blank=True,
    )
