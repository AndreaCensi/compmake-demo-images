import numpy as np

def gray_from_rgb(rgb):
    ''' Converts a HxWx3 RGB image into a HxW grayscale image 
        by computing the luminance. 
        
        :param rgb: RGB image
        :type rgb: array[HxWx3](uint8),H>0,W>0
        
        :return: A RGB image in shades of gray.
        :rtype: array[HxW](uint8)
    '''
    r = rgb[:, :, 0].squeeze()
    g = rgb[:, :, 1].squeeze()
    b = rgb[:, :, 2].squeeze()
    # note we keep a uint8
    gray = r * 299.0 / 1000 + g * 587.0 / 1000 + b * 114.0 / 1000
    return gray


def rgb_from_gray(gray):
    ''' 
        Converts a H x W grayscale into a H x W x 3 RGB image 
        by replicating the gray channel over R,G,B. 
        
        :param gray: grayscale
        :type  gray: array[HxW](uint8),H>0,W>0
        
        :return: A RGB image in shades of gray.
        :rtype: array[HxWx3](uint8)
    '''

    rgb = np.zeros((gray.shape[0], gray.shape[1], 3), dtype='uint8')
    for i in range(3):
        rgb[:, :, i] = gray
    return rgb

