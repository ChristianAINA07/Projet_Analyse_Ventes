import pandas as pd
from sqlalchemy import create_engine

print("=== DEBUT DU CHARGEMENT DANS MYSQL ===")

# 1. Chargement du fichier de données nettoyées
df = pd.read_csv('data/superstore_clean.csv')

# 2. Configuration de la connexion avec Wampserver (MySQL)
# Syntaxe : mysql+mysqlconnector://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE]
# Pour Wampserver par défaut : user='root', password='', host='localhost', port=3306
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/superstore_db')

# 3. Transfert des données vers MySQL
# Création d'une table nommée 'ventes_superstore'
# if_exists='replace' permet de remplacer la table si elle existe déjà
print("Transfert des données en cours... Veuillez patienter...")
df.to_sql(name='ventes_superstore', con=engine, if_exists='replace', index=False)

print("\nDonnées chargées avec succès dans la base 'superstore_db', table 'ventes_superstore' !")
