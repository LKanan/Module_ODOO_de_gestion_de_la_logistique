# Module_ODOO_de_gestion_de_la_logistique
Ce module permet de gérer efficacement les entrées et les sorties des matériels dans une université ou une entreprise et permet aussi de gérer l'établissement des états des besoins matériel. Tout ceci étant garder dans une base de données. La technologie utilisée est l'ERP ODOO.

**PRESENTATION DES DIFFERENTS MENU ET SOUS-MENUS**
- **Logistique_ESIS (menu principal)** <br>
  - Materiels
    - Allouer materiel
    - Enregistrer materiel
  - Demandes
  - Rapports
      - Demandes effectuées
      - Allocations effectuées
  - Autres
    - Mes categories<br>
<br>**EXPLICATION DES DIFFERENTS MENUS ET SOUS-MENUS** <br>
- **Materiels** <br>
  Dans ce menu on gere tout ce qui concerne les entrées et les sorties des materiels.<br>
  Avec son sous-menu **Allouer materiel** là on enregistre les allocations des materiels et lorsqu'on veut allouer un materiel, le logisticien choisi le nom et la categorie du materiel parmi les nom et les categories des materiels qui existent déjà dans la base de données du stock. Apres une allocation la quantité diminue en stock. Et si le materiel est nouveau ou la categorie est nouvelle il a la possibilité de l'ajouter directement à partir de sa vue du formulaire d'allocation.<br>
  Les ***restrictions*** traité pour ce sous-menus sont telles que on le logisticien ne peut pas valider une allocation dans laquelle il a indiqué une quantité de materiel supérieure à la quantité en stock, mais aussi il ne peut pas valider une allocation avec un stock de materiel vide.<br>
  Avec son sous-menu **Enregistrer materiel** on peut ajouter des nouveau materiels en stock ou ajouter la quantité en tock des materiels existants. Ici aussi on spécifie principalement le nom du materiel et choisi la categorie du materiel bien sur si la categorie ne figure pas sur la liste existante on peut l'ajouter directement sur la liste à partir de la vue du formulaire d'enregistrement d'un materiel.<br>
- **Demandes** <br>
  Dans ce menu on gere tout ce qui a rapport avec les demandes des materiels pour alimenter le stock.<br>
On peut faire differnetes demandes en completant le formulaire pour les differentes options principale, la quantité et le prix unitaire, le prix total par rapport à la quantité est calculé automatiquement et principalement on peut aussi specifier pour les differentes demandes si elles sont ***déjà approuvées*** ou pas. Les materiels qui sont listé sont enregistrés dans la liste états des besoins  et aussi si le materiel n'existe pas encore dans la base de données des etats de besoins on peut l'ajouter directement à partir de la vue du formulaire dans lequel on effectue la demande.<br>
- **Rapport** <br>
  Dans ce menu on gere les rapports qu'on peut effectuer.
Avec le sous-menu ***Demandes effectuées*** on peut telecharger la listé de toutes les demandes effectuées pour soit l'imprimer ou l'envoyer comme pièce jointe dans un email de rapport.<br>
Avec le sous-menu ***Allocations effectuées*** on peut telecharger la listé de toutes les allocations effectuées pour aussi soit l'imprimer ou l'envoyer comme pièce jointe dans un email de rapport.
- **Autres** <br>
  Le menu autre nous permet juste de voir la liste des nos categories dans la base de données, et là on peut soit effacer une categorie dans la base de données soit augmenter une categorie.
  


