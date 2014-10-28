

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


def gradient():
    pass