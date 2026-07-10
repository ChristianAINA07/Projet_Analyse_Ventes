import pandas as pd

# ==========================================
# 1. CHARGEMENT ET INSPECTION INITIALE
# ==========================================

# Chargement du fichier CSV
df = pd.read_csv('data/superstore.csv')

print("=== DIAGNOSTIC GLOBAL DES DONNÉES ===")

# Vérification des dimensions
print(f"Dimensions : {df.shape[0]} lignes et {df.shape[1]} colonnes.")

# ==========================================
# 2. ANALYSE DES COLONNES CLÉS
# ==========================================

# Vérification des types de données pour les colonnes importantes
print("\n--- Types des colonnes clés : ---")
colonnes_cles = ['Order.ID', 'Order.Date', 'Sales', 'Profit', 'Quantity']
print(df[colonnes_cles].dtypes)

# Aperçu statistique rapide pour vérifier la cohérence des valeurs numériques
print("\n--- Aperçu statistique des ventes et profits : ---")
print(df[['Sales', 'Profit', 'Quantity']].describe())
