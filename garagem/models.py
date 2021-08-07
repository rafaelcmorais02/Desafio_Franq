from django.db import models
from pessoa.models import PersonCustumer
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from pessoa.models import PersonCustumer
from django.dispatch import receiver

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    CAR = 'C'
    MOTORBIKE = 'M'
    CATEGORY_CHOICES = [
        (CAR, 'Car'),
        (MOTORBIKE, 'Motorbike'),
    ]
    category = models.CharField(
        max_length=1,
        choices=CATEGORY_CHOICES,
        default=CAR,
    )
    def __str__(self):
        return self.name


class Garagem(models.Model):
    person = models.OneToOneField(PersonCustumer, on_delete=models.CASCADE)
    vehicle = models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.person.name
    
    @receiver(post_save, sender=PersonCustumer)
    def create_garage(sender, instance, created, **kwargs):
        if created: 
            Garagem.objects.create(person = instance)
    post_save.connect(create_garage, sender=PersonCustumer)