# SAE-23

SUJET 4 : DRIVE

ce sujet va vous permettre de fournir une interface de gestion d'une ludothèque. Les usagers pourront commenter les jeux et les ajouter dans leur liste personnelle. Le schéma de données est le suivant

- des catégories de produit (id, nom, descriptif)
- des produits (id, nom, date de péremption, photo, marques, auteur,  catégorie)
- des clients (numéro de client, nom, prénom, date d'inscription, adresse)
- des commandes (numéro de commande, client, date)
- une liste de produits d'une commande avec la quantité de chaque produit
- Vous devez implémenter un CRUD pour chacun de ces types de données. vous préparerez la base en avance et la remplirez avec des catégories, des produits et des clients.
- Votre site web devra permettre la saisie de nouveaux clients et de commandes passées sur le drive. Vous devrez aussi pouvoir insérer de nouveaux produits l'aide d'un fichier. La structure du fichier attendu devra bien sur être décrite soit dans une aide, soit en préambule de la page de chargement.

Vous devrez être à même de pouvoir générer une fiche commande avec la liste des produits et le cout total de la commande. indiquer aussi que des produits ne sont plus disponibles ou si la quantité n'est pas suffisante.
