from filesystem import list_categories, list_images
from images_read_write import rgb_write
from instancing import reduce_list_as_tree
from process import average, process_one
import os
    

if __name__ == '__main__':
    # Get the full path to the dataset
    dataset = '101_ObjectCategories'
    output = 'out'
     
    path = os.path.join(dataset, 'Faces_easy')
     
    from compmake import Context
    context = Context()
        
    # List all images in the path
    images = list_images(path) 
    # For each image
    res = []
    for i, image_path in enumerate(images):
        # Process one image
        r = context.comp(process_one, image_path)
        # Save the result promise in a list
        res.append(r)    

    # Compute the average recursively
    f = lambda a,b: context.comp(average, a, b)
    avg = reduce_list_as_tree(f, res)
    
    # write the result
    context.comp(rgb_write, avg, 
                 os.path.join(output, 'faces.jpg'))

    
    import sys
    cmds = sys.argv[1:]
    if cmds:
        context.batch_command(" ".join(cmds))
    else:
        context.compmake_console()
        
        