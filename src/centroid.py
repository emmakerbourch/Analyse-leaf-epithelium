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

import glob

#function for measure centroid
def centroid(img):
    
    #table to measure centroid
    props = measure.regionprops_table(
        img,
        properties=['label', 'centroid'] 
    )
    
    #create a dataframe from the previous table
    df_props = pd.DataFrame(props)
    
    df_props.columns = ['label', 'centroid-x', 'centroid-y']
        
    return df_props