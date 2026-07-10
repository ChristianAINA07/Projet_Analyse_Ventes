-- =========================================================================
-- REQUÊTES D'ANALYSE DES VENTRES ET PROFITS (SUPERSTORE)
-- =========================================================================

-- 1. Calcul du Chiffre d'Affaires total, du profit total et de la quantité vendue
SELECT 
    SUM(Sales) AS Chiffre_Affaires_Total, 
    SUM(Profit) AS Profit_Total, 
    SUM(Quantity) AS Total_Articles_Vendus
FROM ventes_superstore;

-- 2. Classement des marchés (Market) les plus rentables par ordre décroissant
SELECT 
    Market, 
    SUM(Sales) AS Ventes_Par_Marche, 
    SUM(Profit) AS Profit_Par_Marche
FROM ventes_superstore
GROUP BY Market
ORDER BY Profit_Par_Marche DESC;

-- 3. Top 5 des catégories de produits les plus vendues en quantité
SELECT 
    Category, 
    SUM(Quantity) AS Quantite_Vendue
FROM ventes_superstore
GROUP BY Category
ORDER BY Quantite_Vendue DESC
LIMIT 5;
