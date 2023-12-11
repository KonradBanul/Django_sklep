from django.urls import path
from . import views

urlpatterns = [
    path('kategorie/', views.kategoria_list),
    path('kategorie/<int:pk>/', views.kategoria_detail),
    path('kategorie/update/<int:pk>/', views.kategoria_update),
    path('kategorie/delete/<int:pk>/', views.kategoria_delete),
    path('produkty/', views.produkt_list),
    path('produkty/<int:pk>/', views.produkt_detail),
    path('produkty/update/<int:pk>/', views.produkt_update),
    path('produkty/delete/<int:pk>/', views.produkt_delete),
    path('klienci/', views.klient_list),
    path('klienci/<int:pk>/', views.klient_detail),
    path('zamowienia/', views.zamowienie_list),
    path('zamowienia/<int:pk>/', views.zamowienie_detail),
    path('klienci/register/', views.klient_register),
]
