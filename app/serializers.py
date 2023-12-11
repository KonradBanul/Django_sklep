from rest_framework import serializers
from .models import Kategoria, Produkt, Klient, Zamowienie


class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = '__all__'


class ProduktSerializer(serializers.ModelSerializer):
    kategoria = KategoriaSerializer()

    class Meta:
        model = Produkt
        fields = '__all__'


class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['id', 'nazwa', 'password', 'email', 'adres']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email_data = validated_data.pop('email', None)
        adres_data = validated_data.pop('adres', None)

        klient = Klient(nazwa=validated_data['nazwa'])
        klient.set_password(validated_data['password'])
        klient.save()
        if email_data:
            klient.email = email_data
        if adres_data:
            klient.adres = adres_data
        klient.save()
        return klient


class ZamowienieSerializer(serializers.ModelSerializer):
    produkt = ProduktSerializer(many=True)
    klient = KlientSerializer()

    class Meta:
        model = Zamowienie
        fields = '__all__'
