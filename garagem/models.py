from django.db import models
from pessoa.models import PersonCustomer
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
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
    person = models.ForeignKey(PersonCustomer, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15)
    vehicle = models.ManyToManyField(Vehicle)

    def __str__(self):
        return self.person.name
    
    @receiver(post_save, sender=PersonCustomer)
    def create_garagem(sender, instance, created, **kwargs):
        if created: 
            Garagem.objects.create(id = instance.id, person = instance, email = instance.email, phone = instance.phone)
    post_save.connect(create_garagem, sender=PersonCustomer)