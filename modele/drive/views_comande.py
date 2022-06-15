from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import commandeform, commandeonlyform
from . import models

# Create your views here.

def home(request):
    return render(request, "drive/commande/index.html")

def ajout(request, id):
    form = commandeform()
    return render(request, "drive/commande/ajout.html", {"form": form, "id": id})

def ajout_only(request):
    form = commandeonlyform()
    return render(request, "drive/commande/ajout_only.html", {"form": form})

def traitement(request, id):
    client = models.client.objects.get(pk=id)
    form = commandeform(request.POST)
    if form.is_valid():
        commande = form.save(commit=False)
        commande.client = client
        commande.client_id = id
        commande.save()
        return redirect('affiche_client', id=id)
    else:
        return render(request, "drive/commande/ajout.html", {"form": form})

def traitement_only(request):
    form = commandeonlyform(request.POST)
    if form.is_valid():
        commande = form.save()
        return render(request, "drive/commande/affiche.html", {"commande" : commande})
    else :
        return render(request, "drive/commande/affiche.html", {"form" : form})

def affiche(request, id):
    commande = models.commande.objects.get(pk=id)
    return render(request, "drive/commande/affiche.html", {"commande":commande})

def infos(request):
    liste = list(models.commande.objects.all())
    return render(request, "drive/commande/infos.html", {"liste": liste})

def update(request, id):
    commande = models.commande.objects.get(pk=id)
    form = commandeform(commande.dico())
    return render(request, "drive/commande/update.html",{"form":form, "id":id})

def updatetraitement(request, id):
    pform = commandeform(request.POST)
    if pform.is_valid():
        client = pform.save(commit=False)
        client.id = id
        client.client = models.commande.objects.get(pk=id).client
        client.save()
        return HttpResponseRedirect("/affiche_client/" + str(models.commande.objects.get(pk=id).client_id) + "/")
    else:
        return render(request, "/drive/client/update.html", {"form": pform, "id":id})

def delete(request, id):
    commande = models.commande.objects.get(pk=id)
    commande_id = str(models.commande.objects.get(pk=id).client_id)
    commande.delete()
    return HttpResponseRedirect("/affiche_client/" + commande_id + "/")

