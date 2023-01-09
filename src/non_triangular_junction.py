import napari
import pandas as pd
import numpy as np
import tifffile
import skimage
from skimage import data
from skimage import measure
from skimage.morphology import disk
from skimage.filters import median
from skimage import morphology
import skimage.filters as filters

from skimage.morphology import convex_hull_image
from skimage.measure import regionprops_table
from skimage.util import map_array
import seaborn as sns #télécharger seaborn
import matplotlib.pyplot as plt

import skimage.data
import skimage.filters
from napari.types import LabelsData
from skimage.filters import threshold_otsu 
from skimage.morphology import skeletonize
from skimage.morphology import square, cube 
import skimage.filters.rank as rank
import sklearn
from sklearn.neighbors import NearestNeighbors
from skimage import color
from tifffile import imread


def non_triangular_junction (df_junction) :
    # List of all the centroids coordinates:
    centroids = np.array([list(df_junction["centroid-0"]),list(df_junction["centroid-1"])]).T

    # Find the nearest neighbors
    X = centroids
    nbrs = NearestNeighbors(n_neighbors=2, algorithm="ball_tree").fit(X)
    distances, indices = nbrs.kneighbors(X)

    # Find non triangular junctions
    j4 = np.unique(indices[distances[:, 1] < 5])

    # Centroids coordinates of non triangular junctions
    df_nnt_junction = df_junction[df_junction["label"].isin(j4)]
    return(df_nnt_junction)