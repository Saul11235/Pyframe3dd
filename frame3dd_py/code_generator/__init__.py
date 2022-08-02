# code generator 
# for frame3dd input files


try:    from .__all_classes__ import __all_classes__
except: from __all_classes__  import __all_classes__

try:    from .FUNC_concatenate_code import concatenate
except: from FUNC_concatenate_code  import concatenate

exceptions=[
        "FUNC_data_to_string.py",
        "FUNC_concatenate_code.py",
        "DEF_element.py",
        "DEF_node.py"
        ]
requeriments=__all_classes__(exceptions)

#---------------------------------------------

class input_code_class(requeriments):
    
    def __init__(self):
        self.reset()

    def reset(self):
        #use ccomments on string
        self.use_comments=True

        self.structure_name    = "created by frame3dd_py"
        self.shear_effects     = 0
            # 0 - dont include shear effects 
            # 1 - include shear  effects
        self.geometry_stiffness = 0                         
            # 0 - do not include geometry stiffness efects
            # 1 - include geometry stiffness effects

        self.number_of_nodes    = 0
        self.list_nodes         = []


    def get_code(self): return concatenate(self)

