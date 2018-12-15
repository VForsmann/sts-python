import scipy.stats as sst
import pandas as pd
import functions as fn
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA
import plotly.figure_factory as ff
import plotly as py

data = fn.load_data('../../data_preparation/data_preparation.csv')
data = data.select_dtypes(exclude=['object'])
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
# 1 kategorisieren
# hotti = preprocessing.OneHotEncoder()
# hotti.fit(data)

# Z-Transformation
no_z_transformation = ['f2', 'catalogue', 'internet', 'other', 'f12 and so on', 'f13_1', 'f13_2', 'f13_3', 'f20', 'f21']

data[['age', 'f17', 'f1']] = sst.zscore(data[['age', 'f17', 'f1']])
filter_columns = ['age_category', 'f26', 'f22', 'f23_1', 'f23_2', 'f23_3', 'f23_4', 'f25_2']
data = data.drop(columns=filter_columns)

# Faktorenanalyse
pca = PCA(n_components=4)
principalComponents = pca.fit_transform(data)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4'])
print(principalDf)


cluster = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
data['cluster'] = cluster.fit_predict(data)
# kmeans = KMeans(n_clusters=4, random_state=0, max_iter=100).fit(principalDf)
# labels = kmeans.labels_
# data['cluster'] = labels
# cluster_one = data[data['cluster'] == 1]

dendro = ff.create_dendrogram(data)
dendro['layout'].update({'width': 800, 'height': 500})
py.offline.plot(dendro, filename='../html/htmlGraphs/dendrogram.html')
for c in data.columns:
    print("---- %s ---" % c)
    print(data[c].value_counts())
# print(silhouette_score(data, data['cluster']))
