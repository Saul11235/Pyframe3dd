# code generator 
# for frame3dd input files


try:    from .__all_classes__ import __all_classes__
except: from __all_classes__  import __all_classes__

try:    from .concatenate_code import concatenate
except: from concatenate_code  import concatenate

try:
    from .structural_object_classes import object_node
    from .structural_object_classes import object_element
    from .structural_object_classes import object_load_case
except:
    from structural_object_classes import object_node
    from structural_object_classes import object_element
    from structural_object_classes import object_load_case

exceptions=[
        "concatenate_code",
        "object_classes"
        ]
requeriments=__all_classes__(exceptions)

#---------------------------------------------

class input_code_class(requeriments):
    
    def __init__(self):
        #self.__structural_object=structural_object_classes
        self.class_node      = object_node.class_node
        self.class_element   = object_element.class_element
        self.class_load_case = object_load_case.class_load_case
        self.reset()

    def reset(self):
        #use ccomments on string
        self.use_comments=False

        self.structure_name    = "created by frame3dd_py"
        self.shear_effects     = 0
            # 0 - dont include shear effects 
            # 1 - include shear  effects
        self.geometry_stiffness = 0                         
            # 0 - do not include geometry stiffness efects
            # 1 - include geometry stiffness effects
        self.exageration_static = 1    
            # factor for static mesh deformations
        self.scale_for_3d_plot  = 1     
            # factor zoom scale for 3d ploting
        self.increment_axis_x   = -1
            #  len gth of x axis inclement for frmae  element internal force data
            #  if  self.increment_axis_x= -1 internal force are  skipped
        
        # data nodes
        self.number_of_nodes    = 0  #nodes know coordinates, radius and DOF
        self.list_nodes         = [] # [  object_node ,  object_node ..]

        # element nodes
        self.number_of_elements = 0  #elements know all mechanical properties
        self.list_elements      = [] # [  object_element  ]

        # load cases
        self.number_of_load_cases = 1  #max 30 load cases
        self.current_load_case    = self.class_load_case()
        self.list_load_cases      = [] # []

        #  dynamic analisys
        self.number_of_dynamic_modes = 0
            # if number_of_dynamic_modes = 0 the analisys must be only static
            # 

        
 
    def get_code(self): return concatenate(self)

