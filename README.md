# Projet : Analyse des ventes d'une PME 

## Objectif

Le but de ce projet est d'analyser les ventes d'une PME sur une période donnée afin de :

* Calculer le chiffre d'affaires total
* Identifier les ventes par produit
* Identifier les ventes par région
* Suivre l'évolution du chiffre d'affaires par jour

## Étapes réalisées

### 1. Préparation des données

* Importation du fichier CSV fourni par le client.
* Vérification et nettoyage des données, en supprimant notamment les lignes fantômes ou doublons.
* Calcul du chiffre d'affaires pour chaque vente (`prix * qte`).

### 2. Analyse SQL

* Création de la table `ventes` dans SQLiteOnline.
* Exécution des requêtes SQL suivantes :

  1. Chiffre d'affaires total
  2. Ventes par produit (quantité et chiffre d'affaires)
  3. Ventes par région (chiffre d'affaires)
  4. Chiffre d'affaires par jour
* Sauvegarde de toutes les requêtes dans `analyse_ventes.sql`.

### 3. Analyse Python et visualisation

* Chargement des données avec Pandas.
* Filtrage des éventuelles lignes fantômes.
* Calcul du chiffre d'affaires par ligne.
* Création des graphiques interactifs avec Plotly :

  * `ventes-par-produit.html` : ventes par produit (quantité)
  * `ca-par-produit.html` : chiffre d'affaires par produit (€)
* Les fichiers HTML sont exportés et peuvent être consultés dans un navigateur.

## Livrables

* `ventes.csv` : fichier source des ventes.
* `analyse_ventes.sql` : requêtes SQL pour l'analyse.
* `analyse_ventes.py` : script Python pour visualisation.
* `ventes-par-produit.html` et `ca-par-produit.html` : graphiques interactifs.
* `synthese.md` : fiche synthèse des résultats.

## Conclusion

Ce projet permet d'avoir une vision claire des ventes de la PME et d'identifier les produits et régions les plus performants, ainsi que l'évolution quotidienne du chiffre d'affaires. Les graphiques permettent une visualisation rapide et interactive des données pour faciliter la prise de décision.
