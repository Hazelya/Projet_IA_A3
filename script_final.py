# Importation
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from commonFunction import createMap, readCSV


def finalFunction(n_clusters):
    """
    Fonction du script final :
    Affiche la carte des hauteurs totale des arbres en 2 ou 3 catégories en prenant en compte les anomalies.
    :param n_clusters: nombre de clusters à ajouter au model
    :return: /
    """

    # Préparation des données
    data = readCSV()
    df = pd.DataFrame()

    # Pour fonctionner sur les deux bases de données
    if 'longitude' in data.columns and 'latitude' in data.columns:
        df = data[['longitude', 'latitude', 'haut_tot']]
        df.rename(columns={'longitude': 'x'}, inplace=True)
        df.rename(columns={'latitude': 'y'}, inplace=True)
    elif 'x' in data.columns and 'y' in data.columns:
        df = data[['x', 'y', 'haut_tot']]

    target = data[['haut_tot']].values

    # Model KMeans
    kmeansModel = KMeans(n_clusters=n_clusters)
    df['clusters'] = kmeansModel.fit_predict(target)

    # Initialisation pour les anomalies
    X_anomalies = data[['age_estim', 'tronc_diam', 'haut_tronc']]
    anomalies = pd.DataFrame(columns=['anomalie'])

    # Model IsolationForest
    isolationModel = IsolationForest(contamination=0.02)
    anomalies['anomalie'] = isolationModel.fit_predict(X_anomalies)

    # Préparation pour l'affichage
    df_anomalie = df.copy()
    df_anomalie['affichage'] = None
    for i in range(len(df_anomalie)):
        if i < len(anomalies) and anomalies.loc[i, "anomalie"] == -1:
            df_anomalie.loc[i, 'affichage'] = "anomalie"
        elif df_anomalie.loc[i, 'clusters'] == 0:
            df_anomalie.loc[i, 'affichage'] = "Petit"
        elif df_anomalie.loc[i, 'clusters'] == 1:
            df_anomalie.loc[i, 'affichage'] = "Moyen"
        elif df_anomalie.loc[i, 'clusters'] == 2:
            df_anomalie.loc[i, 'affichage'] = "Grand"

    # Creation de la carte
    createMap(df_anomalie, 'affichage')


if __name__ == '__main__':

    finalFunction(3)
