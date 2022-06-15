from django.urls import path
from . import views, views_produit, views_categorie, views_client, views_comande, views_listecommande

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
    path('ajout_client/', views_client.ajout, name=('ajout_client')),
    path('traitement_client/', views_client.traitement, name=('traitement_client')),
    path('infos_client/', views_client.infos, name=('infos_client')),
    path('affiche_client/<int:id>/', views_client.affiche, name=('affiche_client')),
    path('update_client/<int:id>/', views_client.update, name=('update_client')),
    path('updatetraitement_client/<int:id>/', views_client.updatetraitement, name=('updatetraitement_client')),
    path('delete_client/<int:id>/', views_client.delete, name=('delete_client')),
    #URL commandes
    path('ajout_commande/<int:id>/', views_comande.ajout, name=('ajout_commande')),
    path('ajout_commande_only/', views_comande.ajout_only, name=('ajout_commande_only')),
    path('traitement_commande/<int:id>/', views_comande.traitement, name=('traitement_commande')),
    path('traitement_commande_only/', views_comande.traitement_only, name=('traitement_commande_only')),
    path('infos_commande/', views_comande.infos, name=('infos_commande')),
    path('affiche_commande/<int:id>/', views_comande.affiche, name=('affiche_commande')),
    path('update_commande/<int:id>/', views_comande.update, name=('update_commande')),
    path('updatetraitement_commande/<int:id>/', views_comande.updatetraitement, name=('updatetraitement_commande')),
    path('delete_commande/<int:id>/', views_comande.delete, name=('delete_commande')),
    path('ajout_commande_suite/<int:id>/', views_comande.ajout_only_suite, name=('ajout_commande_suite')),

    #URL listecommande
    path('ajout_listecommande/', views_listecommande.ajout, name=('ajout_listecommande')),
    path('traitement_listecommande/', views_listecommande.traitement, name=('traitement_listecommande')),
    path('infos_listecommande/', views_listecommande.infos, name=('infos_listecommande')),
    path('affiche_listecommande/<int:id>/', views_listecommande.affiche, name=('affiche_listecommande')),
    path('update_listecommande/<int:id>/', views_listecommande.update, name=('update_listecommande')),
    path('updatetraitement_listecommande/<int:id>/', views_listecommande.updatetraitement, name=('updatetraitement_listecommande')),
    path('delete_listecommande/<int:id>/', views_listecommande.delete, name=('delete_listecommande')),
]