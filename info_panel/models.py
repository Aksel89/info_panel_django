from django.db import models
from django.core.validators import RegexValidator


class MuseumVisitors(models.Model):
    firstName = models.CharField(verbose_name='Имя',
                                  max_length=50)
    lastName = models.CharField(verbose_name='Фамилия',
                                 max_length=80)
    patronymic = models.CharField(verbose_name='Отчество',
                                  max_length=80,
                                  blank=True)
    email = models.EmailField(max_length=254,
                              unique=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex],
                                   max_length=16, unique=True)
