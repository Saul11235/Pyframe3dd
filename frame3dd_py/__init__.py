#
#  python package for structural  modeling 
#  using the frame3dd  program
#
#  frame3dd program project page:
#  http://frame3dd.sourceforge.net/
#
#  frame3dd_py package
#  
#

try:    from .__all_classes__ import __all_classes__
except: from __all_classes__ import __all_classes__

# add subclasses in current path
__exceptions_class_herency=[]
__class_for_herency=__all_classes__(__exceptions_class_herency)

class  structure(__class_for_herency):

    def __init__(self):
        # system variables
        self.frame3dd_command="frame3dd"

        print("created new structure")



