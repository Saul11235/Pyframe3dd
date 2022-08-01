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

try:    from .__all_classes__ import __all_classes__
except: from __all_classes__  import __all_classes__

try:    from .code_generator import input_code_class 
except: from code_generator  import input_code_class

#creating class for generate  code ------------------------

class input_code(input_code_class):
    pass

# creatin class for structural modeling -------------------

exceptions=[
        "code_generator",
        ]
class_for_heritage=__all_classes__(exceptions)

class  structure(class_for_heritage):
    def __init__(self):
        # system variables
        self.frame3dd_command="frame3dd"
        print("created new structure")



