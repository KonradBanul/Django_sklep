from rest_framework import generics
from .models import Kategoria, Produkt, Klient, Zamowienie
from .serializers import KategoriaSerializer, ProduktSerializer, KlientSerializer, ZamowienieSerializer


class KategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer


class KategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer


class ProduktListCreateView(generics.ListCreateAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer


class ProduktRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produkt.objects.all()
    serializer_class = ProduktSerializer


class KlientListCreateView(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class KlientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer


class ZamowienieListCreateView(generics.ListCreateAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer


class ZamowienieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienie.objects.all()
    serializer_class = ZamowienieSerializer
