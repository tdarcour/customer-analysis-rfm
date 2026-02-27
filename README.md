📊 Customer Analysis with RFM Segmentation
🧠 Contexte du projet

Ce projet a pour objectif d’analyser le comportement des clients à partir de données transactionnelles afin de mieux comprendre la répartition du chiffre d’affaires, identifier les clients à forte valeur et mettre en évidence les clients à risque.

L’analyse repose sur une segmentation RFM (Recency, Frequency, Monetary) et se termine par la création d’un dashboard Power BI destiné à une lecture métier.

🎯 Objectifs

Analyser les données clients et transactions

Nettoyer et préparer les données pour l’analyse

Mettre en place une segmentation RFM

Identifier les segments de clients clés

Visualiser les résultats via un dashboard Power BI

🗂️ Données utilisées

Les données proviennent d’un jeu de données transactionnelles clients et ont été agrégées pour obtenir :

des indicateurs par client (nombre de commandes, montant total dépensé, quantités)

des métriques RFM (Recency, Frequency, Monetary)

Fichiers principaux :

customer_aggregates.csv

rfm_clients.csv

🔎 Démarche analytique

Le projet est structuré en plusieurs étapes, chacune documentée dans un notebook Jupyter :

Exploration des données
Analyse de la structure des données, types de variables, valeurs manquantes.

Nettoyage des données
Suppression des lignes non exploitables, correction des types de données, création de variables utiles.

Analyse descriptive
Calcul des indicateurs clés (chiffre d’affaires, nombre de clients, panier moyen, etc.).

Segmentation RFM

Recency : nombre de jours depuis le dernier achat

Frequency : nombre de commandes

Monetary : montant total dépensé
Attribution de segments clients (Top Clients, Standard, Clients à risque).

Synthèse et interprétation métier
Mise en évidence des segments les plus contributeurs au chiffre d’affaires.

📈 Résultats clés

Une minorité de clients génère la majorité du chiffre d’affaires (logique de Pareto).

Les Top Clients représentent le segment le plus stratégique.

Les Clients à risque contribuent faiblement au chiffre d’affaires et nécessitent des actions de réactivation.

La segmentation RFM constitue une base pertinente pour des actions marketing ciblées.

📊 Dashboard Power BI

Un dashboard Power BI a été réalisé pour faciliter la lecture métier :

KPI :

Chiffre d’affaires total

Nombre de clients

Graphique :

Chiffre d’affaires par segment client

Le fichier Power BI est disponible dans le dossier :

powerbi/

🧮 Analyse SQL

Les données ont également été intégrées dans une base de données relationnelle (SQLite) afin de reproduire un contexte proche de celui rencontré en entreprise.

Des requêtes SQL ont permis de :
- calculer le chiffre d’affaires total
- analyser le chiffre d’affaires par segment client
- déterminer le nombre de clients par segment
- calculer le panier moyen
- identifier les 10 clients générant le plus de chiffre d’affaires

Cette étape permet de valider les indicateurs métiers directement au niveau de la base de données.

🛠️ Stack technique

Python (pandas, numpy)

Jupyter Notebook (via Visual Studo Code)

Power BI Desktop

Git / GitHub

🚀 Pistes d’amélioration

Analyse temporelle plus détaillée (saisonnalité, évolution mensuelle)

Ajout d’indicateurs de rétention client

Intégration d’autres sources de données (marketing, géographie)

Automatisation du pipeline de données

👤 Auteur

Projet réalisé par Tristan Darcourt-Germain
Dans le cadre d’un parcours de montée en compétences en Data Analysis / Business Intelligence.
