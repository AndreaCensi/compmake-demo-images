from filesystem import list_categories
from instancing import instance_categories
import os


if __name__ == '__main__':
    # Get the full path to the dataset
    dataset = os.path.realpath('101_ObjectCategories')
    output = os.path.realpath('out')
     
    from compmake import Context
    context = Context()
    
    categories = context.comp(list_categories, dataset)
    context.comp_dynamic(instance_categories, categories, output)
    
    import sys
    cmds = sys.argv[1:]
    if cmds:
        context.batch_command(" ".join(cmds))
    else:
        context.compmake_console()
        
        