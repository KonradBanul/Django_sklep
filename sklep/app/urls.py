from django.urls import path
from .views import KategoriaListCreateView, KategoriaRetrieveUpdateDestroyView, \
    ProduktListCreateView, ProduktRetrieveUpdateDestroyView, KlientListCreateView, \
    KlientRetrieveUpdateDestroyView, ZamowienieListCreateView, ZamowienieRetrieveUpdateDestroyView

urlpatterns = [
    path('kategorie/', KategoriaListCreateView.as_view(), name='kategoria-list-create'),
    path('kategorie/<int:pk>/', KategoriaRetrieveUpdateDestroyView.as_view(), name='kategoria-retrieve-update-destroy'),
    path('produkty/', ProduktListCreateView.as_view(), name='produkt-list-create'),
    path('produkty/<int:pk>/', ProduktRetrieveUpdateDestroyView.as_view(), name='produkt-retrieve-update-destroy'),
    path('klienci/', KlientListCreateView.as_view(), name='klient-list-create'),
    path('klienci/<int:pk>/', KlientRetrieveUpdateDestroyView.as_view(), name='klient-retrieve-update-destroy'),
    path('zamowienia/', ZamowienieListCreateView.as_view(), name='zamowienie-list-create'),
    path('zamowienia/<int:pk>/', ZamowienieRetrieveUpdateDestroyView.as_view(),
         name='zamowienie-retrieve-update-destroy'),
]
