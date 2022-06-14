from django.urls import path
from . import views, views_produit, views_categorie

urlpatterns = [
    path('', views.home, name='home'),
    #URL produits
    path('ajout_produit/<int:id>/', views_produit.ajout, name=('ajout_produit')),
    path('ajout_produit_only/', views_produit.ajout_only, name=('ajout_produit_only')),
    path('traitement_produit/<int:id>/', views_produit.traitement, name=('traitement_produit')),
    path('traitement_produit_only/', views_produit.traitement_only, name=('traitement_produit_only')),
    path('infos_produit/', views_produit.infos, name=('infos_produits')),
    path('affiche_produit/<int:id>/', views_produit.affiche, name=('affiche_produit')),
    path('update_produit/<int:id>/', views_produit.update, name=('update_produit')),
    path('updatetraitement_produit/<int:id>/', views_produit.updatetraitement, name=('updatetraitement_produit')),
    path('delete_produit/<int:id>/', views_produit.delete, name=('delete_produit')),
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