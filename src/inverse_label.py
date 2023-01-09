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

#loop : read all image (example: .tif)
import glob

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


def inverse_label(label):
    inversed_mask = label.copy()
    inversed_mask[label==0] = 1
    inversed_mask[label!=0] = 0
    return inversed_mask