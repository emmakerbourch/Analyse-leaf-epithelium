import napari
import tifffile
import skimage
from skimage import data
from skimage import measure
import pandas as pd
import numpy as np
from skimage.morphology import disk
from skimage.filters import median
import skimage.filters as filters
from skimage import morphology
    #threshold
import skimage.filters as filters
from skimage import morphology


def segmentation_group3(fnames):
    #remove the third dimension (color)
    fnames_img = tifffile.imread(fnames)
    cells_uncolored = skimage.color.rgb2gray(fnames_img) #source: https://datacarpentry.org/image-processing/03-skimage-images/
    
    # Preprocessing
    med = median(cells_uncolored, disk(8))
    
    # Processing
    
    #threshold
    block_size = 131
    local_threshold = filters.threshold_local(med, block_size=block_size)
    mask_process = med> local_threshold
    
    #remove_small_holes
    mask_process_hole = morphology.remove_small_holes(mask_process.astype(bool), 1000)

    #remove_small_objects
    final_mask = skimage.morphology.remove_small_objects(mask_process_hole, 1000)
    
    # Post-processing
    label_img = skimage.morphology.label(final_mask)
    
    return label_img