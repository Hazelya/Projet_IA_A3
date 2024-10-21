# Created by Julia AZEAU

# Import
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import os
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score


# ___________                   __  .__
# \_   _____/_ __  ____   _____/  |_|__| ____   ____
# |    __)|  |  \/    \_/ ___\   __\  |/  _ \ /    \
# |     \ |  |  /   |  \  \___|  | |  (  <_> )   |  \
# \___  / |____/|___|  /\___  >__| |__|\____/|___|  /
#     \/             \/     \/                    \/

def metriqueOneModel(target, model):
    """
    metrique pour un model
    :param df:
    :param target:
    :param function:
    :return:
    """

    # Score
    silhouette = silhouette_score(target, model.labels_)
    dbs = davies_bouldin_score(target, model.labels_)
    chs = calinski_harabasz_score(target, model.labels_)

    return [silhouette, dbs, chs]

def metrique_nclusters(df, target, function):
    """
    metrique pour un model et pour n clusters
    :param df:
    :param target:
    :param function:
    :return:
    """
    # Initialisation
    n_clusters = [2, 3, 4, 5, 6]
    df_metrique = pd.DataFrame(columns=['n_clusters', 'Silhouette', 'Davies Bouldin', 'Calinski Harabasz'])

    # Pour diverses clusters on test un model
    for i in range(len(n_clusters)):

        # Appel de la fonction du model choisie
        _, model = function(df, target, n_clusters=n_clusters[i])

        # Score
        silhouette = silhouette_score(target, model.labels_)
        dbs = davies_bouldin_score(target, model.labels_)
        chs = calinski_harabasz_score(target, model.labels_)

        # Ajout des scores dans un dataframe
        tab = [silhouette, dbs, chs]
        df_metrique.loc[i + 1] = [n_clusters[i], tab[0], tab[1],
                                  tab[2]]  # contient sous forme de data frame les metriques

    return df_metrique


def readCSV():
    """
    Permet de lire le fichier CSV et le renvoie sous forme d'un data frame
    :return:
    """
    """ Obliger de faire comme ca sinon il est perdue """
    # Récupérer le chemin absolu du script actuel
    script_dir = os.path.dirname(__file__)
    # Construire le chemin absolu du fichier CSV
    csv_path = os.path.join(script_dir, 'Patrimoine_Arbore_nettoye.csv')
    # Lire le fichier CSV
    return pd.read_csv(csv_path)


def graphiqueCluster(df, n_clusters):
    """
    Graphique des clusters
    :param df:
    :param n_clusters:
    :return:
    """
    # Initialisation
    plt.figure()
    colormap = np.array(['Red', 'green', 'blue'])

    # Pour chaque cluster == 0 puis == 1 ...
    for cluster in range(n_clusters):
        df_dun_cluster = df[df['clusters'] == cluster]  # if le cluster de df == au cluster de la boucle
        plt.scatter(df_dun_cluster['x'], df_dun_cluster['y'], c=colormap[cluster], label=cluster)

    plt.legend()
    plt.show()


def createMap(df, color='clusters'):
    """
    Map des clusters
    :param df:
    :return:
    """
    # Préparation des paramètres de la carte
    fig = px.scatter_mapbox(df,
                            lat='y',
                            lon='x',
                            color=color,
                            size_max=15,
                            zoom=10)
    fig.update_layout(mapbox_style="open-street-map")

    # Affichage de la carte
    fig.show()

