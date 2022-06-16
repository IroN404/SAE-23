from django.forms import ModelForm, widgets
from django.utils.translation import gettext_lazy as _
from . import models


#Categorie-------------------------------------------------------------
class categorieform(ModelForm):
    class Meta:
        model = models.categorie
        fields = "__all__"
        labels = {
            'nom' : _('Nom'),
            'details' : _('Descriptif'),

        }

#PRODUITS--------------------------------------------------------------
class produitform(ModelForm):
    class Meta:
        model = models.produit
        fields = ('nom','date_peremption', 'photo','marque','auteur','prix','quantite')
        labels = {
            'nom': _('Nom'),
            'date_peremption' : _('Date de péremption'),
            'photo' : _('Photo') ,
            'marque' : _('Marque'),
            'auteur': _('Auteur'),
            'prix': _('prix unitaire'),
            'quantite': _('quantite'),
        }

class produitonlyform(ModelForm):
    class Meta:
        model = models.produit
        fields = ('nom','date_peremption', 'photo','marque','auteur','categorie','prix','quantite')
        labels = {
            'nom': _('Nom'),
            'date_peremption' : _('Date de péremption'),
            'photo' : _('Photo') ,
            'marque' : _('Marque'),
            'auteur': _('Auteur'),
            'categorie': _('Catégorie'),
            'prix': _('prix unitaire'),
            'quantite': _('quantite'),
        }

#CLIENT--------------------------------------------------------------
class clientform(ModelForm):
    class Meta:
        model = models.client
        fields = ('nom','prenom', 'date_inscription','adresse')
        labels = {
            'nom': _('Nom'),
            'prenom' : _('Prenom'),
            'date_inscription' : _('Date Inscription') ,
            'adresse' : _('Adresse')
        }

#commande-------------------------------------------------------------
class commandeform(ModelForm):
    class Meta:
        model = models.commande
        fields = ('numcommande', 'date')
        labels = {
            'numcommande' : _('Numéro de la commande'),
            'date' : _('Date de la commande'),

        }

class commandeonlyform(ModelForm):
    class Meta:
        model = models.commande
        fields = ('numcommande', 'date','client')
        labels = {
            'numcommande' : _('Numéro de la commande'),
            'date' : _('Date de la commande'),
            'client': _('Nom du client'),

        }

#listecommande--------------------------------------------------------------
class listecommandeform(ModelForm):
    class Meta:
        model = models.listecommande
        fields = ('commande', 'quantite','produit')
        labels = {
            'commande' : _('Nom du client :'),
            'quantite' : _('Quantite du produit :'),
            'produit': _('Produit :'),

        }