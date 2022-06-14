from django.urls import path
from . import views_produit, views_categorie

urlpatterns = [
    #URL produits
    path('', views_produit.home, name='home'),
    # URL catégorie
    path('ajout_categorie/', views_categorie.ajout, name=('ajout_categorie')),
    path('traitement_categorie/', views_categorie.traitement, name=('traitement_categorie')),
    path('infos_categorie/', views_categorie.infos, name=('infos_categorie')),
    path('affiche_categorie/<int:id>/', views_categorie.affiche, name=('affiche_categorie')),
    path('update_categorie/<int:id>/', views_categorie.update, name=('update_categorie')),
    path('updatetraitement_categorie/<int:id>/', views_categorie.updatetraitement, name=('updatetraitement_categorie')),
    path('delete_categorie/<int:id>/', views_categorie.delete, name=('delete_categorie')),
    #URL clients
    #URL commandes
]