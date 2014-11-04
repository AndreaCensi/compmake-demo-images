from images_read_write import imread
from operations import rgb_from_gray
import numpy as np
 
def process_cat(path, out):
    from filesystem import list_images
    images = list_images(path) 
    # For each image
    res = []
    for image_path in images:
        # Process one image
        r = process_one(image_path)
        # Save the result promise in a list
        res.append(r)    

    # Compute the average recursively

    from instancing import reduce_list_as_tree
    avg = reduce_list_as_tree(average, res)

    # write the result
    from images_read_write import rgb_write
    rgb_write(avg, out) 


def process_one(filename):
    # read the image
    rgb = imread(filename)
    # convert to grayscale
    if rgb.ndim == 2:
        rgb = rgb_from_gray(rgb)
    
    # resize to (64, 64)
    #print(rgb.shape)
    x = rgb_smooth(rgb, sigma=3)
    #print(x.shape)
    x = rgb_resize(x, (128, 128))
    #print(x.shape)
    return x

def rgb_resize(rgb, shape):
    from scipy.misc import imresize
    res = np.zeros((shape[0], shape[1], 3))
    for i in range(3):
        res[:,:,i] = imresize(rgb[:,:,i], shape, interp='bilinear', mode='F')
    return res

def rgb_smooth(rgb, sigma):
    from scipy.ndimage import gaussian_filter
    res = np.empty_like(rgb)
    for i in range(3):
        res[:,:,i] = gaussian_filter(rgb[:,:,i], sigma=sigma)
    return res

def average(image1, image2):
    return image1*0.5 + image2*0.5
    
    
