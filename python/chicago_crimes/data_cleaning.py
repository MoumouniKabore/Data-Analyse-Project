import pandas as pd

data = [
    "data_origin/Chicago_Crimes_2001_to_2004.csv",
    "data_origin/Chicago_Crimes_2005_to_2007.csv",
    "data_origin/Chicago_Crimes_2008_to_2011.csv",
    "data_origin/Chicago_Crimes_2012_to_2017.csv",
]

fichiers = []

for dt in data:

    print(f"\n----- Nettoyage du fichier {dt[12:39]} -----\n")

    print(f"Lecture et chargement du fichier '{dt[12:39]}.csv'...\n")
    df = pd.read_csv(dt, engine='python', on_bad_lines='skip', encoding='utf-8')

    nombre_doublons = df.duplicated().sum()

    if (nombre_doublons != 0):
        dbl = "s"
    else:
        dbl = ""

    # ***********

    # Afficher le nombre de ligne, colonne et doublon
    print(f"Nombre de ligne : {df.shape[0]} lignes")
    print(f"Nombre de colonne : {df.shape[1]} colonnes")
    print(f"Nombre de doublon : {nombre_doublons} doublon{dbl}")

    # Suppression des variables dont je n'utiliserai pas
    print("\nSuppression de certaine variable...")
    df.drop(columns={'Unnamed: 0', 'ID', 'Case Number', 'Block', 'IUCR', 'Beat', 'Ward', 'Community Area', 'X Coordinate', 'Y Coordinate', 'Year', 'Location'}, inplace=True)

    # Suppression des doublons
    print("\nSuppression des doublons...")
    if (nombre_doublons == 0):
        print("Pas de doublon à supprimer\n")
    else:
        df.drop_duplicates(inplace=True)
        print("Doublon supprimer.\n")

    # Afficher le nouveau nombre de ligne, colonne et doublon (Vérification) 
    print(f"Nouveau nombre de ligne : {df.shape[0]} lignes")
    print(f"Nouveau nombre de colonne : {df.shape[1]} colonnes")
    if (nombre_doublons > 0):
        print(f"Nouveau nombre de doublon : {df.duplicated().sum()} doublon")
        
    print("\n\tValeurs null.")
    print(df.isnull().sum())
    print("\nSupression des Valeurs null...")
    df.dropna(inplace=True)
    print("\n\tValeur null supprimer.")
    print(df.isnull().sum())

    # ************

    print("\nConversion des types de certaine variable...")
    
    print("\t* Changement du type de la variable 'District' de float à str...")
    df['District'] = df['District'].astype(str).str.replace('.0', '')

    dates = ['Date', 'Updated On']
    for date in dates:
        if (df[date].dtype != 'datetime64[us]'):
            print(f"\t* Changement du type de la variable '{date}' de str à date...")
            df[date] = pd.to_datetime(df[date], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

    coordonnes = ['Latitude', 'Longitude']
    for coordonne in coordonnes:
        if (df[coordonne].dtype != 'float64'):
            print(f"\t* Changement du type de la variable '{coordonne}' de str à float...")
            df[coordonne] = pd.to_numeric(df[coordonne], errors='coerce')
    
    # ************

    print("\nExtraction et création des variables Heure, Jour, Mois et Année...")

    print("\t* Création de la variable 'Hour'...")
    df['Hour'] = df['Date'].dt.strftime('%H').astype(int)

    print("\t* Création de la variable 'Day'...")
    df['Day'] = df['Date'].dt.day_name()

    print("\t* Création de la variable 'Month'...")
    df['Month'] = df['Date'].dt.strftime('%B')

    print("\t* Création de la variable 'Year'...")
    df['Year'] = df['Date'].dt.strftime('%Y')

    # ************

    print("\nPetit résumer des informations du Dataframe :")
    print(df.info())

    # ************

    nom_nouveau_fichier = "data_" + dt[27:39]
    print(f"\nCréation du fichier {nom_nouveau_fichier}.parquet...")
    df.to_parquet(nom_nouveau_fichier + ".parquet", index=False)

    # ************

    fichiers.append(nom_nouveau_fichier + ".parquet")

    # ************
    # ************
    # ************

print("\n----- Création du fichier csv complet -----\n")

print("Association des nouveaux fichiers...\n")
df_fusion = pd.concat(map(pd.read_parquet, fichiers), ignore_index=True)

print("Création du fichier complet combinant tous les fichiers .parquet (final_data_chicago_crimes_2001_to_2017.parquet)...\n")
df_fusion.to_parquet("final_data_chicago_crimes_2001_to_2017.parquet", index=False)