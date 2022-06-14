from django.urls import path
from . import views_produit, views_categorie

urlpatterns = [
    #URL produits
    path('', views_produit.home, name='home'),

    #URL clients
    #URL commandes
]