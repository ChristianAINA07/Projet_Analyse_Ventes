import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

print("=== DEBUT DE LA PREDICTION DES VENTES (MACHINE LEARNING) ===")

# 1. Chargement des données nettoyées
df = pd.read_csv('data/superstore_clean.csv')

# 2. Sélection des variables (Features et Target)
X = df[['Quantity', 'Profit']]
y = df['Sales']

# 3. Division des données (80% pour l'entraînement, 20% pour le test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialisation et entraînement du modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Évaluation du modèle sur les données de test
predictions = model.predict(X_test)
rmse = root_mean_squared_error(y_test, predictions)

print("\nModèle entraîné avec succès !")
print(f"Erreur moyenne de prédiction (RMSE) : {rmse:.2f} USD")
