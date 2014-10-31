from filesystem import  list_images
from process import average, process_one
import os


def instance_categories(context, categories, output):
    for category, path in categories.items():
        context.comp_dynamic(instance_category, category, path, output,
                            job_id=category) 

def instance_category(context, category, path, out):
    # List all images in the path
    images = list_images(path) 
    # For each image
    res = []
    for i, image_path in enumerate(images):
        # Process one
        r = context.comp(process_one, image_path,
                        job_id='%s-%s' % (category, i))
        # Save the result in a list
        res.append(r)
        
    # Compute the average recursively
    
    # Schedule merging of two images 
    op = lambda a,b: context.comp(average, a, b)
    # Recursively create tree
    avg = reduce_list_as_tree(op, res)
    
    from images_read_write import rgb_write
    context.comp(rgb_write, avg, 
                 os.path.join(out, '%s.jpg' % category))


def reduce_list_as_tree(op, res):
    if len(res) == 0:
        msg = 'Empty list'
        raise ValueError(msg)
    if len(res) == 1:
        return res[0]
    if len(res) == 2:
        return op(res[0], res[1])
    half = len(res)/2
    first = reduce_list_as_tree(op, res[:half])
    second = reduce_list_as_tree(op, res[half:])
    return op(first, second)

