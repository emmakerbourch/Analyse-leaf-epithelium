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


def total_junctions(mask):
    
    # Reduce the number of pixel of the mask
    skeleton = skeletonize(mask)

    # Convert the label to the good type
    img = skeleton.astype(np.uint8) 

    # Find neighboor pixel
    img2 = rank.sum(img, square(3))
    mask_junction = img2.copy()

    # Find junctions (less than 2 pixel is considered as a non jonction)
    mask_junction[img2 > 3] = 1
    mask_junction[img2 <= 3] = 0

    # Label all junctions 
    labelled = skimage.morphology.label(mask_junction)

    
    props = measure.regionprops_table(
        labelled,
        properties=['label',"centroid"] 
        )

    df_junction = pd.DataFrame(props)
    
    # Count the total number of junctions
    total_nb_junctions= len(df_junction["label"])
    
    return df_junction, total_nb_junctions