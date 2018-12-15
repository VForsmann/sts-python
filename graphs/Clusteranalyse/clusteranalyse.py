from sklearn.cluster import KMeans
import pandas as pd
import functions as fn
import matplotlib.pyplot as plt

data = fn.load_data('../../data_preparation/data_preparation.csv')


#kmeans = KMeans(n_clusters=4)
#kmeans.fit(data[['f26', 'f1']])
#y_kmeans = kmeans.predict(data[['f26', 'f1']])

#plt.scatter(data['f26'], data['f1'], c=y_kmeans, s=50, cmap='viridis')

#centers = kmeans.cluster_centers_plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)


#plt.scatter(data['f6_1'], data['f6_2'], s=50);
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(data[['f26', 'f17', 'f1']])
y_kmeans = kmeans.predict(data[['f26', 'f17', 'f1']])

plt.scatter(data['f26'], data['f17'], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.show()

