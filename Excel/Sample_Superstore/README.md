Lien du fichier csv utiliser : https://www.kaggle.com/datasets/naveenkumar20bps1137/sample-superstore

Le fichier csv :
- J'ai eu à modifier le fichier csv en faisant des remplacements, comme par exemple remplacer les virgules suivie d'espace ', ' par un espace ' '.
Lors de l'importation du fichier csv dans power query, le délimiteur utiliser est la virgule, une virgule qui n'a pas d'espace avant et après, or dans la variable "Product Name", certain nom contient des virgules, power query utilise alors ces virgules comme délimiteur, cela crée un décalage des données. Dans cette même variable, il y a des noms qui ont des virgules sans espace avant ni après, eu n'ont pas pu être remplacer, alors j'ai enlever ces virgules manuellement.
- J'ai aussi remplacer le caractère guillement '"' (se trouvant dans la colonne "Product Name") par un espace ' ', j'ai remarqué que lorsqu' il est présent, les lignes conténant ce caractère ne sont pas bien importer.

Nétoyage des données (Power query) :
- J'ai changé les types des variables "Row ID" et "Postal Code" du type entier au type text.
- La colonne "Order Date" était de type texte avec pour format "Mois/Jours/Années", d'abord, j'ai fractionné cette colonne par le délimoteur "/", j'ai obtenu trois colonne que j'ai nommé "Mois", "Jours" et "Années" et ensuite j'ai créer une nouvelle colonne "Order Date" avec ces trois colonne réuini mais cette fois au format "Jours/Mois/Années". Même méthode pour la colonne "Ship Date".
- J'ai ajouter deux colonnes "Profit Margin" pour la marge bénéficiare par commande et "Delivery Time", le delais de livraison.

La feuille excel -> Tableau de bord
- Réduire le ruban
- Zoomer à 100%