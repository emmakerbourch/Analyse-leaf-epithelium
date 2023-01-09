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


#function to measure the convex hull preimeter of each labeled image
def convex_hull_perimeter(img):
    convex_hull = skimage.morphology.convex_hull_image(img)
    convex_hull_perimeter = measure.perimeter(convex_hull)
    
    return convex_hull_perimeter


#function to calculate the lobeyness of each labeled image
def lobeyness_per_species(species_folder, species_name):
    
    df = pd.DataFrame()
    
    for fnames in glob.glob(species_folder + "*.tif"):
        img = tifffile.imread(fnames)
        
        #create a table
        props = skimage.measure.regionprops_table(
            img,
            properties = ('label', 'area', 'perimeter'),
            extra_properties = (convex_hull_perimeter,) # measure the convex hull of each labeled image
        )
        
        #transform in dataframe
        df2 = pd.DataFrame(props)
        df = pd.concat([df, df2])
        df = df.assign(lobeyness = df['perimeter']/df["convex_hull_perimeter"])
    
    #calculate lobeyness, add to the DataFrame
    df = df.assign(species = f'{species_name}')
    df = df.reset_index(drop = True)
    return df