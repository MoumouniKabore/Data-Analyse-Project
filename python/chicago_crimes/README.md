Lien des fichiers .csv utiliser : https://www.kaggle.com/datasets/abhisheksinghblr/chicago-crime

Au départ, l'objectif du fichier data_cleaning.py n'était pas de réaliser un nettoyage complet des données, mais simplement de supprimer les doublons présent dans chaque fichier avant de les fusionner. Cependant, au fur et à mesure de l'avancement du projet, je me suis rendu compte qu'il était également nécessaire de supprimer les valeurs nulles, modifier le type et bien d'autres action. Le script a donc évolué pour effectuer le nettoyage de chaque fichier, puis les fusionner en un seul fichier de données propre et prêt pour l'analyse

COMMENT EXÉCUTER LE FICHIER "data_cleaning.py"
- Créer un dossier nommé "chicago_crimes".
- À l'intérieur du dossier chicago_crimes, créer un dossier nommé "data_origin" qui contiendra les 4 fichiers .csv télécharger sur le lien en haut (Chicago_Crimes_2001_to_2004.csv, Chicago_Crimes_2005_to_2007.csv, Chicago_Crimes_2008_to_2011.csv, Chicago_Crimes_2012_to_2017.csv)
- Ajouter dans le dossier chicago_crimes, le fichier "data_cleaning.py" et exécuter ce fichier python
- L'exécution du fichier data_cleaning.py créera 4 fichiers .parquet nettoyer et ensuite un fichier final combinant les 4 fichier .parquet en un "final_data_chicago_crimes_2001_to_2017.parquet" déjà nettoyer.