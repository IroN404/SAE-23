from django.db import models

#PRODUIT-----------------------------------------------------------------
class produit(models.Model):
    nom = models.CharField(max_length=100)
    date_peremption = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to ='media/',blank=True)
    marque = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey("categorie", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nom} de {self.marque}, périme le {self.date_peremption}. Catégorie : {self.categorie}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "date_peremption": self.date_peremption, "photo": self.photo, "marque": self.marque, "auteur": self.auteur, "categorie": self.categorie}

#CATEGORIE----------------------------------------------------------------
class categorie(models.Model):
    nom = models.CharField(max_length=20)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

    def dico(self):
        return {"nom": self.nom, "details": self.details}