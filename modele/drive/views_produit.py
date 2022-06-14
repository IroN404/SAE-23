from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import produitform, categorieform
from . import models

# Create your views here.

def home(request):
    return render(request, "drive/produit/index.html")

def ajout(request, id):
    form = produitform()
    return render(request, "drive/produit/ajout.html", {"form": form, "id": id})

def traitement(request, id):
    produit = models.produit.objects.get(pk=id)
    pform = produitform(request.POST)
    if pform.is_valid():
        produit = pform.save(commit=False)
        produit.save()
        return redirect('affiche', id=id)
    else:
        return render(request, "drive/produit/ajout.html", {"form": pform})

def affiche(request, id):
    produit = models.produit.objects.get(pk=id)
    return render(request, "drive/produit/affiche.html", {"produit":produit})

def infos(request):
    liste = list(models.produit.objects.all())
    return render(request, "drive/produit/infos.html", {"liste": liste})

def update(request, id):
    produit = models.produit.objects.get(pk=id)
    form = produitform(produit.dico())
    return render(request, "drive/produit/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    pform = produitform(request.POST)
    if pform.is_valid():
        categorie = pform.save(commit=False)
        categorie.id = id
        categorie.categorie_id = models.produit.objects.get(pk=id).categorie_id
        categorie.save()
        return HttpResponseRedirect("drive/categorie/affichecategorie/" + str(models.produit.objects.get(pk=id).categorie_id) + "/")
    else:
        return render(request, "drive/categorie/update.html", {"form": pform, "id":id})

def delete(request, id):
    produit = models.produit.objects.get(pk=id)
    produit_id = str(models.produit.objects.get(pk=id).categorie_id)
    produit.delete()
    return HttpResponseRedirect("drive/categorie/affichecategorie/" + produit_id + "/")