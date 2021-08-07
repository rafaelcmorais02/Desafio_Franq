from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class PersonCustumer(models.Model):
    categoria = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15)

    def __str__(self):
        return self.name
