from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ["nazwa"]


class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField()

    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ["nazwa"]


class UserManager(BaseUserManager):
    def create_user(self, nazwa, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(nazwa=nazwa, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nazwa, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(nazwa, email, password, **extra_fields)


class Klient(AbstractUser):
    username = None
    nazwa = models.CharField(unique=True, max_length=100, blank=False)
    email = models.EmailField(unique=True, max_length=100, blank=False)
    adres = models.TextField()

    objects = UserManager()
    USERNAME_FIELD = "nazwa"

    def __str__(self):
        return self.nazwa

    class Meta:
        ordering = ["nazwa"]


class Zamowienie(models.Model):
    produkt = models.ManyToManyField(Produkt)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Zamowienie: {self.id} - {self.klient.nazwa} - data: {self.data_zamowienia}"
