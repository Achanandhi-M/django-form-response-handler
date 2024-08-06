from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


loginValidator=RegexValidator(
r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$", "Only alphanumeric characters and - are allowed."
)
class Login(models.Model):
    userName=models.CharField(unique=True,max_length=20,validators=[loginValidator])
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.userName
        