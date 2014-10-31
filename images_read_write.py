import numpy as np
import os


def imread(filename):
    ''' 
        Reads an image from a file into a numpy array. This can have
        different dtypes according to whether it's RGB, grayscale, RGBA, etc.
        
        :param filename: Image filename.
        :type filename: string
        
        :return: image: The image as a numpy array.
        :rtype: image
    '''
    from PIL import Image  # @UnresolvedImport
    try:
        im = Image.open(filename)
    except Exception as e:
        msg = 'Could not open filename "%s": %s' % (filename, e)
        raise ValueError(msg)

    data = np.array(im)

    return data
 
 
def rgb_write(rgb, filename):
    # create directory if it doesn't exist
    d = os.path.dirname(filename)
    if not os.path.exists(d):
        os.makedirs(d)
    # create rgb from float in [0,1]
    rgb = rgb.astype('uint8')
    # write the file
    imwrite(rgb, filename)


def imwrite(rgb, filename):
    im = image_from_array(rgb)
    im.save(filename)    


def image_from_array(rgb):
    ''' Converts an image in a numpy array to an Image instance.
        Accepts:  h x w      255  interpreted as grayscale
        Accepts:  h x w x 3  255  rgb  
        Accepts:  h x w x 4  255  rgba '''
    from PIL import Image  # @UnresolvedImport
    a = rgb
    if not a.dtype == 'uint8':
        raise ValueError('I expect dtype to be uint8, got "%s".' % a.dtype)
 
    if len(a.shape) == 2:
        height, width = a.shape
        rgba = np.zeros((height, width, 4), dtype='uint8')
        rgba[:, :, 0] = a
        rgba[:, :, 1] = a
        rgba[:, :, 2] = a
        rgba[:, :, 3] = 255
    elif len(a.shape) == 3:
        height, width = a.shape[0:2]
        depth = a.shape[2]
        rgba = np.zeros((height, width, 4), dtype='uint8')
        if not depth in [3, 4]:
            raise ValueError('Unexpected shape "%s".' % str(a.shape))
        rgba[:, :, 0:depth] = a[:, :, 0:depth]
        if depth == 3:
            rgba[:, :, 3] = 255
    else:
        raise ValueError('Unexpected shape "%s".' % str(a.shape))
     
    im = Image.frombuffer("RGBA", (width, height), rgba.data,
                           "raw", "RGBA", 0, 1)
    return im