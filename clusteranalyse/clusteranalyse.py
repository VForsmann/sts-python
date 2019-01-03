import pandas as pd
import functions as fn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import factor_analyzer as kaiser
import plotly.figure_factory as ff
import plotly as plotly
import plotly.graph_objs as go

def calculate_cluster():
    data = pd.read_csv('./data_preparation/data_preparation.csv', sep=';', na_values='Nothing', error_bad_lines=False, index_col=0)
    raw_data = fn.load_data('./data_preparation/data_preparation.csv')
    data = data.select_dtypes(exclude=['object'])
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)

    # Z-Transformation (Wird nicht mehr benoetigt)
    # data[['f4_12', 'f4_13', 'f5_7', 'f5_8', 'f10_1', 'f10_2', 'f18_7', 'f18_9', 'f19_8']] =
    # sst.zscore(data[['f4_12', 'f4_13', 'f5_7', 'f5_8', 'f10_1', 'f10_2', 'f18_7', 'f18_9', 'f19_8']])

    # Entscheiden der Variablen, nach denen Geclustert werden soll.
    columns_for_clustering = ['f4_12', 'f4_13', 'f5_7', 'f10_1', 'f10_2', 'f18_2', 'f18_7', 'f19_8']

    # Ueberpruefen der Werte für die Faktorenanalyse mithilfe des Kaiser Kriteriums
    print(kaiser.calculate_kmo(data[columns_for_clustering]))

    # Faktorenanalyse mit 3 Faktoren
    pca = PCA(n_components=3)
    factor_components = pca.fit_transform(data[columns_for_clustering])
    factor_df = pd.DataFrame(data=factor_components, columns=['first', 'second', 'third'])

    # Ueberpruefen der optimalen Clusteranzahl
    Sum_of_squared_distances = []
    K = range(1, 15)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(factor_df)
        Sum_of_squared_distances.append(km.inertia_)
    graph = plotly.graph_objs.Scatter(y=Sum_of_squared_distances, x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    plotly.offline.plot([graph], filename='./graphs/html/htmlGraphs/optimal-cluster.html')

    # Erstellen der Cluster mithilfe des KMeans Algorithmus
    kmeans = KMeans(n_clusters=3, random_state=0, max_iter=500).fit(factor_df)
    raw_data['cluster'] = kmeans.labels_
    print(kmeans.labels_)

    # Ueberpruefen der Silhouette vom Kmeans
    print(silhouette_score(factor_df, kmeans.labels_))

        # Fuer Vitus, hier sind die Faktoren drin fuer den 3D graphen
    print(factor_df)
    clustered = factor_df.assign(cluster=pd.Series(kmeans.labels_))
    first_cluster = clustered.loc[clustered['cluster'] == 0]
    second_cluster = clustered.loc[clustered['cluster'] == 1]
    third_cluster = clustered.loc[clustered['cluster'] == 2]

    trace0 = {
    'x': first_cluster['first'].values,
    'y': first_cluster['second'].values,
    'z': first_cluster['third'].values,
    "marker": {
        "color": "#A020F0", 
        "size": 5
    },
    "opacity": 0.7, 
    "mode": "markers", 
    "name": "Cluster 1", 
    "type": "scatter3d"
    }

    trace0cluster = {
    'x': first_cluster['first'].values,
    'y': first_cluster['second'].values,
    'z': first_cluster['third'].values, 
    "alphahull" : 5,
    "opacity": 0.3,
    "type": "mesh3d",
    "color": "#A020F0",
    "name": "Cluster 1"
    }

    trace1 = {
    'x': second_cluster['first'].values,
    'y': second_cluster['second'].values,
    'z': second_cluster['third'].values,
    "marker": {
        "color": "#8B1A1A", 
        "size": 5
    }, 
    "opacity": 0.7,
    "mode": "markers", 
    "name": "Cluster 2", 
    "type": "scatter3d"
    }

    trace1cluster = {
    'x': second_cluster['first'].values,
    'y': second_cluster['second'].values,
    'z': second_cluster['third'].values, 
    "alphahull" : 5,
    "opacity": 0.3,
    "type": "mesh3d",
    "color": "#8B1A1A",
    "name": "Cluster 2"
    }

    trace2 = {
    'x': third_cluster['first'].values,
    'y': third_cluster['second'].values,
    'z': third_cluster['third'].values,
    "marker": {
        "color": "#008B45", 
        "size": 5
    }, 
    "opacity": 0.7,
    "mode": "markers", 
    "name": "Cluster 3", 
    "type": "scatter3d"
    }

    trace2cluster = {
    'x': third_cluster['first'].values,
    'y': third_cluster['second'].values,
    'z': third_cluster['third'].values, 
    "alphahull" : 5,
    "opacity": 0.3,
    "type": "mesh3d",
    "color": "#008B45",
    "name": "Cluster 3"
    }

    data = [trace0, trace1, trace2, trace0cluster, trace1cluster, trace2cluster]
    layout = dict(
        title = 'Robinson Kundencluster'
    )
    fig = dict( data=data, layout=layout )
    # Use py.iplot() for IPython notebook
    plotly.offline.plot(fig, filename='./graphs/html/htmlGraphs/3dCluster.html')

    # Erstellen des Dendrogramms
    dendro = ff.create_dendrogram(factor_df)
    dendro['layout'].update({'width': 800, 'height': 500})
    plotly.offline.plot(dendro, filename='./graphs/html/htmlGraphs/dendrogramm.html')

    # Funktion zum erklaeren der Cluster
    for c in raw_data.columns:
        print("---- %s ---" % c)
        print(raw_data[c][raw_data['cluster']==0].value_counts())
        print(raw_data[c][raw_data['cluster']==1].value_counts())
        print(raw_data[c][raw_data['cluster']==2].value_counts())

    # Cluster 0: Kinderlose großverdiener, Genießer, steigert nicht das wohlbefinden, würden nicht mehr zahlen, bevorzugen
    # kein bio vor konventioenneln, kaufen eher kein bio, nicht wichtig (Öko essen), Ehepartner ausflug
    # CLuster 1: Großverdiener, gesundheitsorientiert, nicht abschrecken, steigert wohlbefinden, würden draufzahlen,
    # bevorzugen bio bei kindern, bevorzugen bio , kaufen Bio eher mittel, Öko essen ist im urlaub wichtig, Sport ebenfalls,
    # Familien
    # Cluster 2: Großverdiener, Gebildete Menschen, weltoffen/Genießer, abschrecken ist eher neutral, neutral wohlbefinden,
    # würden nicht mehr zahlen für bio, bio ist kein gutes preis/leistungverhältnis, Siegel wichtig, hochwertige aber keine
    # abwechslungsreiche nahrung, wichtig bei kindern, eher gleichgültig bei der eigenen, gleichgültige bevorzugung, kaufen
    # es nicht im alltag, Preis wichtig, Guetesiegel ebenfalls, Öko essen egal im urlaub, Feel good extrem wichtig,
    # Sehr kiderfreundlich, sehr sportlich
