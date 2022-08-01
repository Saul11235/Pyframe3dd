# code generator 
# for frame3dd input files

try:    from .__all_classes__ import __all_classes__
except: from __all_classes__  import __all_classes__

exceptions=[
        "element.py",
        "node.py"
        ]
requeriments=__all_classes__(exceptions)

class input_code_class(requeriments):
    
    def __init__(self):
        #vars
        self.__structure_name    = "created by frame3dd_py"
        self.__shear_effects     = 0
            # 0 - dont include shear effects 
            # 1 - include shear  effects
        self.__geometry_stiffness = 0                         
            # 0 - do not include geometry stiffness efects
            # 1 - include geometry stiffness effects

        
        


