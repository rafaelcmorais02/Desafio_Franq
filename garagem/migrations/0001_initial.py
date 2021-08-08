# Generated by Django 3.2.6 on 2021-08-08 03:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('C', 'Car'), ('M', 'Motorbike')], default='C', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Garagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.personcustomer')),
                ('vehicle', models.ManyToManyField(to='garagem.Vehicle')),
            ],
        ),
    ]
