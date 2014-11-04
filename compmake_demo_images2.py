from filesystem import list_images, list_categories
from images_read_write import rgb_write
from instancing import reduce_list_as_tree
from process import average, process_one
import os
from process import process_cat

   

if __name__ == '__main__':
    # Get the full path to the dataset
    dataset = '101_ObjectCategories'
    output = 'out'
    
    from compmake import Context
    context = Context()
        
    cats = list_categories(dataset)
    for category, path in cats.items():
        out = os.path.join(output, '%s.jpg' % category)
        context.comp(process_cat, path, out, job_id=category) 

    import sys
    cmds = sys.argv[1:]
    if cmds:
        context.batch_command(" ".join(cmds))
    else:
        context.compmake_console()
        
        
        
