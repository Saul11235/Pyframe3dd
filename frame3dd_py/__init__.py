#
#  python package for structural  modeling 
#  using the frame3dd  program
#
#  frame3dd program project page:
#  http://frame3dd.sourceforge.net/
#
#  frame3dd_py package
#  Edwin Saul PM
#

try:    from .code_generator import input_code_class 
except: from code_generator  import input_code_class

class input_code(input_code_class):
    pass

#---------------------------------------------------

try:    from .model_structure import class_structure
except: from model_structure  import class_structure

class  structure(class_structure):
    pass



