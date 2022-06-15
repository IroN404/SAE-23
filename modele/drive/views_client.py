from django.shortcuts import render, HttpResponseRedirect
from .forms import clientform
from . import models
# Create your views here.

def ajout(request):
    if request.method == 'POST':
        form = clientform(request)
        return render(request,"drive/client/ajout.html", {"form":form})
    else:
        form = clientform()
        return render(request, "drive/client/ajout.html", {"form": form})

def traitement(request):
    form = clientform(request.POST)
    if form.is_valid():
        client = form.save()
        return HttpResponseRedirect("/infos_client")
    else :
        return render(request,"drive/client/ajout.html",{"form": form})

def infos(request):
    liste = list(models.client.objects.all())
    return render(request,"drive/client/infos.html", {"liste" : liste})

def affiche(request, id):
    client = models.client.objects.get(pk=id)
    liste = models.commande.objects.filter(client_id = id)
    return render(request, "drive/client/affiche.html", {"client":client, "liste" : liste})

def update(request, id):
    categorie = models.client.objects.get(pk=id)
    form = clientform(categorie.dico())
    return render(request, "drive/client/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    form = clientform(request.POST)
    if form.is_valid():
        client = form.save(commit=False)
        client.id = id
        client.save()
        return HttpResponseRedirect("/infos_client")
    else:
        return render(request, "drive/client/update.html", {"form": form, "id":id})

def delete(request, id):
    client = models.client.objects.get(pk=id)
    commande = models.commande.objects.filter(client_id = id)
    client.delete()
    commande.delete()
    return HttpResponseRedirect("/infos_client/")