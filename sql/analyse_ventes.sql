-- 🔹 SQL : Analyse des ventes d'une PME

-- Chiffre d'affaires total
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;

-- Ventes par produit
SELECT 
    produit,
    SUM(qte) AS total_vendu,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY chiffre_affaires DESC;

-- Ventes par région
SELECT 
    region,
    SUM(prix * qte) AS chiffre_affaires_region
FROM ventes
GROUP BY region
ORDER BY chiffre_affaires_region DESC;

-- Chiffre d'affaires par jour
SELECT 
    date,
    SUM(prix * qte) AS chiffre_affaires_jour
FROM ventes
GROUP BY date
ORDER BY date ASC;