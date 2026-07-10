import pandas as pd

# ==========================================
# 1. CHARGEMENT DES DONNÉES
# ==========================================
print("=== DEBUT DU NETTOYAGE DES DONNÉES ===")
df = pd.read_csv('data/superstore.csv')

# ==========================================
# 2. TRAITEMENT DES COLONNES
# ==========================================

# Remplacement des points par des underscores dans les noms des colonnes
df.columns = df.columns.str.replace('.', '_', regex=False)

# Suppression de la colonne avec les caractères chinois
if '记录数' in df.columns:
    df = df.drop(columns=['记录数'])

# ==========================================
# 3. CONVERSION DES TYPES DE DONNÉES
# ==========================================

# Conversion des colonnes de dates au format datetime approprié
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], errors='coerce')

# ==========================================
# 4. VÉRIFICATION ET ENREGISTREMENT
# ==========================================

print("\n--- Structure finale après nettoyage : ---")
print(df[['Order_ID', 'Order_Date', 'Sales', 'Profit']].dtypes)

# Sauvegarde du fichier nettoyé dans le dossier data
df.to_csv('data/superstore_clean.csv', index=False)
print("\nFichier nettoyé enregistré avec succès sous 'data/superstore_clean.csv'")
