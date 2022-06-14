from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


#Categorie-------------------------------------------------------------
class categorieform(ModelForm):
    class Meta:
        model = models.categorie
        fields = ('nom','descriptif')
        labels = {
            'nom' : _('Nom'),
            'descriptif' : _('Descriptif'),

        }

#PRODUITS--------------------------------------------------------------
class produitform(ModelForm):
    class Meta:
        model = models.produit
        fields = ('nom','date_peremption', 'photo','marque','auteur','categorie')
        labels = {
            'nom': _('Nom'),
            'date_peremption' : _('Date de péremption'),
            'photo' : _('Photo') ,
            'marque' : _('Marque'),
            'auteur': _('Auteur'),
            'categorie': _('categorie'),
        }