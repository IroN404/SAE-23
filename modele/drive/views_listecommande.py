from django.shortcuts import render, HttpResponseRedirect
from .forms import listecommandeform
from . import models
# Create your views here.

def ajout(request):
    if request.method == 'POST':
        form = listecommandeform(request)
        return render(request,"drive/listecommande/ajout.html", {"form":form})
    else:
        form = listecommandeform()
        return render(request, "drive/listecommande/ajout.html", {"form": form})

def traitement(request):
    form = listecommandeform(request.POST)
    if form.is_valid():
        listecommande = form.save(commit=false)
        return HttpResponseRedirect("/infos_listecommande")
    else :
        return render(request,"drive/listecommande/ajout.html",{"form": form})

def infos(request):
    liste = list(models.listecommande.objects.all())
    return render(request,"drive/listecommande/infos.html", {"liste" : liste})

def affiche(request, id):
    liste = models.listecommande.objects.get(pk=id)
    return render(request, "drive/listecommande/affiche.html", {"liste":liste})

def update(request, id):
    listecommande = models.listecommande.objects.get(pk=id)
    form = listecommandeform(listecommande.dico())
    return render(request, "drive/listecommande/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    form = listecommandeform(request.POST)
    if form.is_valid():
        listecommande = form.save(commit=False)
        listecommande.id = id
        listecommande.save()
        return HttpResponseRedirect("/infos_listecommande")
    else:
        return render(request, "drive/listecommande/update.html", {"form": form, "id":id})

def delete(request, id):
    listecommande = models.listecommande.objects.get(pk=id)
    listecommande.delete()
    return HttpResponseRedirect("/infos_listecommande/")