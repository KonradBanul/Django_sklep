from rest_framework import serializers
from .models import Kategoria, Produkt, Klient, Zamowienie


class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = ('id', 'nazwa')


class ProduktSerializer(serializers.ModelSerializer):
    kategoria = KategoriaSerializer()

    class Meta:
        model = Produkt
        fields = ('id', 'nazwa', 'opis', 'cena', 'kategoria', 'ilosc')


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ('id', 'nazwa', 'email', 'adres')


class ZamowienieSerializer(serializers.ModelSerializer):
    produkt = ProduktSerializer(many=True)
    klient = KlientSerializer()

    class Meta:
        model = Zamowienie
        fields = ('id', 'produkt', 'klient', 'data_zamowienia')
