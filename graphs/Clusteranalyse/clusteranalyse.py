import scipy.stats as sst
import pandas as pd
import functions as fn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import factor_analyzer as kaiser
import plotly.figure_factory as ff
import plotly as plotly

data = pd.read_csv('../../data_preparation/data_preparation.csv', sep=';', na_values='Nothing', error_bad_lines=False, index_col=0)
raw_data = fn.load_data('../../data_preparation/data_preparation.csv')
data = data.select_dtypes(exclude=['object'])
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# Z-Transformation
no_z_transformation = ['f2', 'catalogue', 'internet', 'other', 'f12 and so on', 'f13_1', 'f13_2', 'f13_3', 'f20', 'f21']


# data[['f4_12', 'f4_13', 'f5_7', 'f5_8', 'f10_1', 'f10_2', 'f18_7', 'f18_9', 'f19_8']] = sst.zscore(data[['f4_12', 'f4_13', 'f5_7', 'f5_8', 'f10_1', 'f10_2', 'f18_7', 'f18_9', 'f19_8']])
# Filtern der Spalten, die nicht mit in die Clusteranalyse sollen
filter_columns = ['ID', 'Ort', 'f1', 'f2', 'f3_1', 'f3_2', 'f3_3', 'f3_4', 'f3_5', 'f3_6', 'f3_7', 'f3_8', 'f3_9', 'f3_10', 'f3_11',
                  'f3_txt_val', 'f4_1', 'f4_2', 'f4_3', 'f4_4', 'f4_5', 'f4_6', 'f4_7', 'f4_8', 'f4_9', 'f4_10',
                  'f4_11', 'f4_12', 'f4_13', 'f4_14', 'f4_txt_val', 'f5_1', 'f5_2', 'f5_3', 'f5_4', 'f5_5',
                  'f5_6', 'f5_7', 'f5_8', 'f5_9', 'f5_10', 'f5_11', 'f5_txt_val', 'f6_1', 'f6_2', 'f6_3', 'f6_4',
                  'f6_5', 'f6_6', 'f6_7', 'f6_8', 'f6_9', 'f8', 'f9', 'f10_1', 'f10_2', 'f11_1', 'f11_2', 'f11_3',
                  'f11_4', 'f11_5', 'f11_6', 'f11_7', 'f11_8', 'f11_9', 'f11_10', 'f12_1', 'f12_2', 'f12_3', 'f12_4',
                  'f12_5', 'f12_6', 'f12_7', 'f12_8', 'f12_9',  'f13_1', 'f13_2', 'f13_3',  'f15_1', 'f15_2', 'f15_3',
                  'f15_4', 'f15_5', 'f15_6', 'f15_7', 'f15_8', 'f15_9', 'f15_10', 'f15_11', 'f15_12', 'f15_13',
                  'f15_14', 'f15_15', 'f15_16', 'f15_txt_val', 'f16_1', 'f16_2', 'f16_3', 'f16_4', 'f16_5', 'f16_6',
                  'f16_7', 'f16_8', 'f16_9', 'f17', 'f18_1', 'f18_2', 'f18_3', 'f18_4', 'f18_5', 'f18_6', 'f18_7',
                  'f18_8', 'f18_9', 'f19_1', 'f19_2', 'f19_3', 'f19_4', 'f19_5', 'f19_6', 'f19_7', 'f19_8', 'f19_9',
                  'f19_10', 'f20', 'f21', 'f22', 'f23_1', 'f23_2', 'f23_3', 'f23_4', 'f25_2',
                  'f26', 'age_category',  'income_class', 'catalogue', 'internet', 'other',
                  'age']
columns_for_clustering = ['f4_12', 'f4_13', 'f5_7', 'f10_1', 'f10_2', 'f18_2', 'f18_7', 'f19_8']
# data = data.drop(columns=filter_columns)
# print(data[columns_for_clustering])
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
# plotly.offline.plot([graph], filename='../html/htmlGraphs/optimal-cluster.html')

# Erstellen der Cluster mithilfe des KMeans Algorithmus
kmeans = KMeans(n_clusters=3, random_state=0, max_iter=500).fit(factor_df)

# Hirachisches Cluster
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
cluster.fit(factor_df)
raw_data['cluster'] = kmeans.labels_
print(kmeans.labels_)

# Ueberpruefen der Silhouette vom Kmeans
print(silhouette_score(factor_df, kmeans.labels_))
# Erstellen des Dendrogram
dendro = ff.create_dendrogram(factor_df)
dendro['layout'].update({'width': 800, 'height': 500})
# plotly.offline.plot(dendro, filename='../html/htmlGraphs/dendrogram.html')
for c in raw_data.columns:
  print("---- %s ---" % c)
  print(raw_data[c][raw_data['cluster']==2].value_counts())

# Cluster 0: Kinderlose großverdiener, Genießer, steigert nicht das wohlbefinden, würden nicht mehr zahlen, bevorzugen
# kein bio vor konventioenneln, kaufen eher kein bio, nicht wichtig (Öko essen), Ehepartner ausflug
# CLuster 1: Großverdiener, gesundheitsorientiert, nicht abschrecken, steigert wohlbefinden, würden draufzahlen,
# bevorzugen bio bei kindern, bevorzugen bio , kaufen Bio eher mittel, Öko essen ist im urlaub wichtig, Sport ebenfalls,
# Familien
# Cluster 2: Großverdiener, Gebildete Menschen, weltoffen/Genießer, abschrecken ist eher neutral, neutral wohlbefinden,
# würden nicht mehr zahlen für bio, bio ist kein gutes preis/leistungverhältnis, Siegel wichtig, hochwertige aber keine
# abwechslungsreiche nahrung, wichtig bei kindern eher gleichgültig bei der eigenen, gleichgültige bevorzugung, kaufen
# es nicht im alltag, Preis wichtig, Guetesiegel ebenfalls, Öko essen egal im urlaub, Feel good extrem wichtig,
# Sehr kiderfreundlich, sehr sportlich
