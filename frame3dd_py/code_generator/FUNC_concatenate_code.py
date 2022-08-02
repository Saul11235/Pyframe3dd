# code  generator for frame3dd syntax input file
# by Edwin Saul PM

try:    from .FUNC_data_to_string import data_format
except: from FUNC_data_to_string  import data_format

def concatenate(obj):

    #  function to create source for input to frame3dd

    class class_code:
        def __init__(self)      : self.code_string=""
        def get_code(self)      : return self.code_string
        def write(self,element) :
            self.code_string+=str(element)+"\n"
    obj_code=class_code() ; wr=obj_code.write   
    use_comments=obj.use_comments

    # WRITE STRUCTURE NAME
    wr(obj.structure_name) 

    # WRITE NODE DEFINITIONS
    if not(use_comments) :  
        wr(obj.number_of_nodes)
    else:
        wr("")
        wr(str(obj.number_of_nodes)+" # number.of.nodes")
    table_nodes =  [] ;var =  0
    if use_comments:
        table_nodes+=[["#node","x","y","z","radius"]]
    for Nnode in range(len(obj.list_nodes)):
        obj_node = obj.list_nodes[Nnode]
        l_file   = [Nnode+1]+obj_node.get_coord_list()
        table_nodes.append(l_file)
    wr( data_format(table_nodes)  )

    # NODE RESTRICTIONS
    if not(use_comments) :  
        wr(obj.number_of_nodes)
    else:
        wr("")
        wr(str(obj.number_of_nodes)+" # restricted.nodes")
    table_nodes =  [] ;var =  0
    if use_comments:
        table_nodes+=[["#node","x","y","z","rx","ry","rz"]]
    for Nnode in range(len(obj.list_nodes)):
        obj_node = obj.list_nodes[Nnode]
        l_file   = [Nnode+1]+obj_node.get_restrictions_list()
        table_nodes.append(l_file)
    wr( data_format(table_nodes)  )



    # ELEMENTS


        


    #Set
        



    #----------------------------

    return obj_code.get_code()


