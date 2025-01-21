from django.db import models


class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Produkt(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField()

    def __str__(self):
        return self.nazwa


class Klient(models.Model):
    nazwa = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    adres = models.TextField()

    def __str__(self):
        return self.nazwa


class Zamowienie(models.Model):
    produkt = models.ManyToManyField(Produkt)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zamowienia = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Zamowienie: {self.id} - {self.klient.name}"
