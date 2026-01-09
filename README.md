# Méthode de classification et de visualisation des arbres par taille

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Python](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![Python](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)

Ce projet consiste, après un nettoyage des données en R, à réaliser une classification en trouvant la meilleure méthode de clustering pour visualiser sur une carte le patrimoine arboré de Saint-Quentin selon leurs tailles (nous prenons en compte s'il y a des anomalies).

## Prérequis

Les librairies nécessaires :
- pandas : manipulation de dataframe et de données.
- numpy : calcul numérique.
- matplotlib : statique.
- plotly : visualisation.
- scikit-learn : algorithmes de machine learning et de clustering.
- os : gestion des fichiers et répertoires.

```bash
pip install pandas numpy matplotlib plotly scikit-learn
```

## Commencer

Pour comprendre les recherchers qui nous à pousser a choisir telles méthode et pas une autre je vous conseille de télécharger une extension Jupyter pour lire le notebook.

Si vous voulez simplement voir le résultat, il vous suffit de lancer le script Python.
```bash
python script_final.py
```

Il est possible de réutiliser la map générer pour l'integrer à un site web.

## Description des différents fichiers de codes

### `Notebook.ipynb`
Ce fichier contient le notebook ainsi que les recherches utilisées afin de comprendre, d'appréhender et de réaliser le script final.
Il contient entre autres 3 clusterings différents avec :

1. Un modèle 
2. Un graphique 
3. Une carte 
4. Une comparaison des métriques selon le nombre de clusters (qui aboutit souvent à une recherche du meilleur k clusters)

À la toute fin, une partie est dédiée à la comparaison des différents modèles.
Puis suit une partie sur la recherche pour les anomalies.

### `script_final.py`
Ce fichier contient le script final exécutant le meilleur clustering trouvé : KMeans

Il prend en entrée un nombre de clusters (2 ou 3).

Le script peut être appliqué aux deux jeux de données :
1. Patrimoine_Arbore_nettoye.csv
2. Data_Arbre.csv

Créant ainsi une carte des hauteurs d'arbres avec leurs anomalies.

### `commonFunction.py`
Jupiter et le script final s'appuient sur le document commonFunction.py, 
pour éviter les fonctions répétitives.
On y retrouve les fonctions suivantes :
1. metriqueOneModel : Qui applique les métriques pour un modèle donné.
2. metrique_nclusters : Qui applique pour 2 à 6 clusters les métriques d'un model donnée.
3. readCSV : Permet la lecture d'un fichier CSV.
4. graphiqueCluster : Affiche un graphique des clusters.
5. createMap : Créer et affiche une map des clusters.

## Auteurs 

Azeau Julia : @Hazelya

## Licence

Ce projet est sous licence : **MIT License** - voir le fichier LICENSE pour plus d'informations.
