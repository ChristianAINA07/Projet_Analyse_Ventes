# 📊 Projet End-to-End Data Analytics : Analyse et Prévision des Ventes (Superstore)

Ce projet présente un workflow complet de Data Analyst, allant de l'extraction et du nettoyage des données jusqu'à la modélisation prédictive et la visualisation interactive sous forme de tableau de bord. 

L'objectif est de fournir des insights clés aux décideurs pour optimiser les performances commerciales.

---

## 🛠️ Technologies Utilisées
* **Langage :** Python (v3.13)
* **Librairies :** Pandas, NumPy, Scikit-learn, SQLAlchemy, Mysql-connector
* **Base de Données :** MySQL (via Wampserver / phpMyAdmin)
* **Visualisation :** Power BI Desktop
* **Gestion de Version :** Git & GitHub

---

## 📂 Structure du Projet
```text
Projet_Analyse_Ventes/
│
├── data/                       # Contient les fichiers de données (exclus du suivi Git)
│   ├── superstore.csv          # Jeu de données brut initial
│   ├── superstore_clean.csv    # Données nettoyées via Python
│   └── superstore_clean.xlsx   # Version Excel pour intégration Power BI
│
├── analyse.py                  # Script d'inspection initiale et diagnostic global
├── nettoyage.py                # Script d'ETL (Data Cleaning et transformation)
├── chargement.py               # Script d'automatisation de l'injection dans MySQL
├── requetes.sql                # Requêtes SQL clés d'analyse de performance
├── prediction.py               # Modèle de Machine Learning (Régression Linéaire)
└── Dashboard_Ventes.pbix       # Rapport visuel et interactif Power BI
```

---

## 🚀 Architecture du Workflow (Pipeline ETL & Analyse)

### 1. Collecte et Diagnostic (`analyse.py`)
* Chargement du jeu de données brut de **51 290 lignes et 27 colonnes**.
* Identification des types de données, des anomalies de formatage et de la structure des colonnes.

### 2. Nettoyage et Préparation des Données (`nettoyage.py`)
* Normalisation des noms de colonnes (remplacement des points par des `_` pour la compatibilité SQL).
* Nettoyage des colonnes obsolètes ou contenant des encodages corrompus.
* Conversion des formats de chaînes textuelles en objets `datetime` (`Order_Date`, `Ship_Date`).

### 3. Stockage et Requêtage Relationnel (`chargement.py` & `requetes.sql`)
* Création automatique de la base de données `superstore_db` et injection des données via un moteur **SQLAlchemy** connecté à **Wampserver**.
* Réalisation de requêtes SQL complexes pour extraire :
  * Le Chiffre d'Affaires global et la rentabilité totale.
  * Le classement des marchés mondiaux les plus rentables.
  * Le Top 5 des catégories de produits générant le plus de volume de ventes.

### 4. Visualisation Interactive (Power BI)
* Conception d'un tableau de bord dynamique connecté aux données préparées.
* Intégration d'indicateurs de performance clés (KPIs) : **Chiffre d'Affaires Global (13M)** et **Profit Total**.
* Analyse de la répartition géographique des ventes via une sectorisation par région (*Donut Chart*).

### 5. Modélisation Prédictive (`prediction.py`)
* Implémentation d'un algorithme de **Machine Learning (Régression Linéaire)** avec **Scikit-learn** pour anticiper le volume des ventes futures en fonction des quantités commandées et des marges de profit.
* Partitionnement des données (80% entraînement / 20% test) et évaluation des performances du modèle par le calcul de la racine de l'erreur quadratique moyenne (**RMSE**).

---

## 📈 Résultats du Modèle de Prédiction
* **Algorithme :** Régression Linéaire
* **Indicateur de Performance :** Erreur moyenne de prédiction (RMSE) de **471.29 USD**. 
* *Note : Ce modèle sert de base de référence (Baseline) et peut être optimisé à l'aide d'algorithmes plus complexes comme KNN (K-Nearest Neighbors) ou Random Forest.*
