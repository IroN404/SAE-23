from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import produitform, produitonlyform
from . import models

# Create your views here.

def home(request):
    return render(request, "drive/produit/index.html")

def ajout(request, id):
    form = produitform()
    return render(request, "drive/produit/ajout.html", {"form": form, "id": id})

def ajout_only(request):
    form = produitonlyform()
    return render(request, "drive/produit/ajout_only.html", {"form": form})

def traitement(request, id):
    categorie = models.categorie.objects.get(pk=id)
    form = produitform(request.POST)
    if form.is_valid():
        produit = form.save(commit=False)
        produit.categorie = categorie
        produit.categorie_id = id
        produit.save()
        return redirect('affiche_categorie', id=id)
    else:
        return render(request, "drive/produit/ajout.html", {"form": form})

def traitement_only(request):
    form = produitonlyform(request.POST)
    if form.is_valid():
        produit = form.save()
        return render(request, "drive/produit/affiche.html", {"produit" : produit})
    else :
        return render(request, "drive/produit/affiche.html", {"form" : form})

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
        return HttpResponseRedirect("/affiche_categorie/" + str(models.produit.objects.get(pk=id).categorie_id) + "/")
    else:
        return render(request, "/drive/categorie/update.html", {"form": pform, "id":id})

def delete(request, id):
    produit = models.produit.objects.get(pk=id)
    produit_id = str(models.produit.objects.get(pk=id).categorie_id)
    produit.delete()
    return HttpResponseRedirect("/affiche_categorie/" + produit_id + "/")