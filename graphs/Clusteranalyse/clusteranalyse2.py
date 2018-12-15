import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import functions as fn
from numpy import where

data = fn.load_data('../../data_preparation/data_preparation.csv')

# Plots 2 features, with an output, shows the decision boundary
def plot3D(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    pos = where(y == 1)
    neg = where(y == 0)

    color = ['r', 'b', 'y', 'k', 'g', 'c', 'm']

    for i in range(30):
        ax.scatter(x[i, 0], x[i, 1],x[i, 2], marker='o', c=color[int(y[i])-1])
    #ax.scatter(x[:,1], x[:,2], y)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    axes = plt.axis()
    plt.show()

plot3D(data[['f26', 'f17', 'f1']], 4)