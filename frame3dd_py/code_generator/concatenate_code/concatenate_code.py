# code  generator for frame3dd syntax input file
# by Edwin Saul PM

try:    from .data_to_string import data_format
except: from data_to_string  import data_format

try:    from .write_load_cases import write_load_cases
except: from write_load_cases  import write_load_cases


def concatenate_function(obj):

    #  function to create source for input to frame3dd

    class class_code:
        def __init__(self)      : self.code_string=""
        def get_code(self)      : return self.code_string
        def write(self,element) :
            self.code_string+=str(element)+"\n"
    obj_code=class_code() ; wr=obj_code.write   
    use_comments=obj.use_comments

    # WRITE STRUCTURE NAME  ------------------------
    wr(obj.structure_name) 
    if use_comments: wr("# name of the model")

    # WRITE NODE DEFINITIONS -----------------------
    if not(use_comments) :  
        wr(obj.number_of_nodes)
    else:
        wr("")
        wr(str(obj.number_of_nodes)+" # number of nodes")
    table_nodes =  [] ;var =  0
    if use_comments:
        table_nodes+=[["# node ","x-coord ","y-coord ",
            "z-coord ","radius "]]

    for Nnode in range(obj.number_of_nodes):
        obj_node = obj.list_nodes[Nnode]
        l_file   = [Nnode+1]+obj_node.get_coord_list()
        table_nodes.append(l_file)
    if  obj.number_of_nodes:    
        wr( data_format(table_nodes)  )

    # NODE RESTRICTIONS --------------------------------
    if not(use_comments) :  
        wr(obj.number_of_nodes)
    else:
        wr("")
        wr(str(obj.number_of_nodes)+" # nodes know restr.")
    table_nodes =  [] ;var =  0
    if use_comments:
        table_nodes+=[["# node ","rx ","ry ","rz ",
            "rxx ","ryy ","rzz "]]
    for Nnode in range(obj.number_of_nodes):
        obj_node = obj.list_nodes[Nnode]
        l_file   = [Nnode+1]+obj_node.get_restrictions_list()
        table_nodes.append(l_file)
    if obj.number_of_nodes:    
        wr( data_format(table_nodes) )

    # ELEMENTS ------------------------------------------
    if not(use_comments) :
        wr(obj.number_of_elements)
    else:
        wr("")
        wr(str(obj.number_of_elements)+" # number of elements")
    table_elem =  []; var = 0
    if use_comments:
        table_elem+=[["# element ","n1 ","n2 ",
            "Ax ","Asy ","Asz ","Jx ","Iy ","Iz ",
            "E ","G ","roll ","density"
            ]]
    for Nelement in range(obj.number_of_elements):    
        object_element=obj.list_elements[Nelement]
        l_file=[Nelement+1]+object_element.get_data_element()
        table_elem.append(l_file)
    if  obj.number_of_elements:
        wr(data_format(table_elem))

    # CONFIGS MODEL --------------------------------------
    table_configs=[]
    if use_comments:
        wr("")
        shear_effects = obj.shear_effects; line = []
        if shear_effects:
            line=[1,"# shear effects included"]
        else: 
            line=[0,"# no shear effects included"]   
        table_configs.append(line[:])   
        geometry_stiffness= obj.geometry_stiffness
        if geometry_stiffness:
            line=[1,"# geometry stiffness effects included"]
        else:
            line=[0,"# no geometry stiffness effects included"]
        table_configs.append(line[:])
        x=obj.exageration_static
        line=[x,"# exageration factor for static deformations"]
        table_configs.append(line[:])
        sc=obj.scale_for_3d_plot
        line=[sc,"# zoom scale for 3d ploting"]
        table_configs.append(line[:])
        increment_axis_x=obj.increment_axis_x
        if increment_axis_x==-1:
            line=[-1,"# skip internal forces calculations"]
        else:
            line=[increment_axis_x,
        "# delta x-axis for frame element internal force data"]
        table_configs.append(line[:])    
    else:
        table_configs=[
                [obj.shear_effects],
                [obj.geometry_stiffness],
                [obj.exageration_static],
                [obj.scale_for_3d_plot],
                [obj.increment_axis_x]
                ]
    wr(data_format(table_configs))

    #WRITE LOAD CASES----------------------------
    write_load_cases(wr,obj)

    return obj_code.get_code()


