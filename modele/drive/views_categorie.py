from django.shortcuts import render, HttpResponseRedirect
from .forms import categorieform
from . import models
# Create your views here.

def ajout(request):
    if request.method == 'POST':
        form = categorieform(request)
        return render(request,"drive/categorie/ajout.html", {"form":form})
    else:
        form = categorieform()
        return render(request, "drive/categorie/ajout.html", {"form": form})

def traitement(request):
    form = categorieform(request.POST)
    if form.is_valid():
        categorie = form.save()
        return HttpResponseRedirect("/infos_categorie")
    else :
        return render(request,"drive/categorie/ajout.html",{"form": form})

def infos(request):
    liste = list(models.categorie.objects.all())
    return render(request,"drive/categorie/infos.html", {"liste" : liste})

def affiche(request, id):
    categorie = models.categorie.objects.get(pk=id)
    liste = models.produit.objects.filter(categorie_id = id)
    return render(request, "drive/categorie/affiche.html", {"categorie":categorie, "liste" : liste})

def update(request, id):
    categorie = models.categorie.objects.get(pk=id)
    form = categorieform(categorie.dico())
    return render(request, "drive/categorie/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    form = categorieform(request.POST)
    if form.is_valid():
        categorie = form.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/infos_categorie")
    else:
        return render(request, "drive/categorie/update.html", {"form": form, "id":id})

def delete(request, id):
    categorie = models.categorie.objects.get(pk=id)
    produit = models.produit.objects.filter(categorie_id = id)
    categorie.delete()
    produit.delete()
    return HttpResponseRedirect("/infos_categorie/")