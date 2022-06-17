from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import listecommandeform
from . import models
from fpdf import FPDF
from django.http import FileResponse
# Create your views here.


def ajout(request):
    if request.method == "POST":
        form = listecommandeform(request)
        if form.is_valid():
            listecommande = form.save()
            return render(request,"drive/listecommande/affiche.html",{"listecommande" : listecommande})
        else:
            return render(request,"drive/listecommande/ajout.html",{"form": form})
    else :
        form = listecommandeform()
    return render(request,"drive/listecommande/ajout.html",{"form" : form})


def traitement(request):
    form = listecommandeform(request.POST)
    produit_commande = request.POST["produit"]
    produitstock = models.produit.objects.get(pk=produit_commande)
    quantite = request.POST["quantite"]
    if form.is_valid() and int(produitstock.quantite) >= int(quantite):
        new_quantite = int(produitstock.quantite)-int(quantite)
        models.produit.objects.filter(pk=produit_commande).update(quantite=new_quantite)
        listecommande = form.save(commit=False)
        listecommande.save()
        return render(request, "drive/listecommande/affiche.html", {"listecommande" : listecommande})
    else:
        return render(request,"drive/listecommande/ajout.html",{"alert" : "Veuillez rentré des données cohérentes", "form":form})

def infos(request):
    liste = list(models.listecommande.objects.all())
    return render(request,"drive/listecommande/infos.html",{"liste": liste})

def affiche(request, id):
    listecommande = models.listecommande.objects.get(pk=id)
    prix_produit_commande = listecommande.produit.prix
    quantite_commande = listecommande.quantite
    prix_totale_commande = int(prix_produit_commande)*int(quantite_commande)
    return render(request,'drive/listecommande/affiche.html',{"lp": listecommande,"prix":prix_totale_commande}) #


def update(request, id):
    listecommande = models.listecommande.objects.get(pk=id)
    form = listecommandeform(listecommande.dictionnaire())
    quantitecommande = int(listecommande.produit.quantite) + int(form["quantite"].value())
    models.produit.objects.filter(pk=listecommande.produit.id).update(quantite=quantitecommande) #remet la valeurs initial du stock
    return render(request,'drive/listecommande/ajout.html',{"form": form, "id":id})


def updatetraitement(request, id):
    form = listecommandeform(request.POST)
    produit_commande = request.POST["produit"]
    stock_produit = models.produit.objects.get(pk=produit_commande)
    quantite_commande = request.POST["quantite"]
    if form.is_valid() and int(stock_produit.produit) >= int(quantite_commande):
        new_stock = int(stock_produit.produit)-int(quantite_commande)
        models.produit.objects.filter(pk=produit_commande).update(produit=new_stock)
        listecommande = form.save(commit=False)
        listecommande.id = id
        listecommande.save()
        return HttpResponseRedirect("/infos_listecommande/")
    else:
        return render(request,"drive/listecommande/ajout.html",{"form": form, "id":id})


def delete(request, id):
    listecommande = models.listecommande.objects.get(pk=id)
    listecommande.delete()
    form = listecommandeform(listecommande.dictionnaire())
    stock_produit_commande = int(listecommande.produit.produit) + int(form["quantite"].value())
    models.produit.objects.filter(pk=listecommande.produit.id).update(produit=stock_produit_commande)
    return HttpResponseRedirect("/infos_listecommande/")