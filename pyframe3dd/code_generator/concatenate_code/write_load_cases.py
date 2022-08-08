# code  generator for frame3dd syntax input file
# by Edwin Saul PM


try:    from .data_to_string import data_format
except: from data_to_string  import data_format



def write_a_load_case(obj,number,total,use_comments,wr):

    text=""
    text2=""
    if use_comments:
        text=" load case "+str(number)+" of "+str(total)

        text2="load case "+str(number)

    if use_comments:
        wr("# begin "+text)
    #----------------------------
    # WRITE - GRAVITY 
    line=[]
    if use_comments:
        wr("")
        line.append(["#gx  ","gy  ","gz   "," gravitational  accelaration - "+text2])
    line.append([obj.gX , obj.gY ,  obj.gZ])   
    wr(data_format(line))
    if use_comments: wr("")

    #----------------------------
    # SEE DATA
    data_load_nodes         = obj.load_nodes
    num_load_nodes          = len(data_load_nodes)
    #--------------------------
    data_load_uniformly     = obj.load_uniformly
    num_load_uniformly      = len(data_load_uniformly)
    #--------------------------
    data_trapezoidally_load = obj.trapezoidally_load
    num_trapezoidally_load  = len(data_trapezoidally_load)
    #--------------------------
    data_concentrated_loads = obj.concentrated_interior_loads
    num_concentrated_loads  = len(data_concentrated_loads)
    #--------------------------
    data_temperature_loads  = obj.temperature_loads
    num_temperature_loads   = len(data_temperature_loads)
    #--------------------------
    data_displacements      = obj.prescribed_displacements
    num_displacements       = len(data_displacements)
    #-----------------------------
    # HEADERS 
    headers=[]
    if use_comments:
        list_headers=[
          [num_load_nodes,
              "# num loaded nodes                            - "+text2],
          [num_load_uniformly,
              "# num uniformly distributed element loads     - "+text2],
          [num_trapezoidally_load,
              "# num trapezoidally distributed element loads - "+text2],
          [num_concentrated_loads,
              "# num concentrated interior loads             - "+text2],
          [num_temperature_loads,
              "# num frame element with temperature changes  - "+text2],
          [num_displacements,
              "# num prescribed displacements                - "+text2]


                ]
        headers=data_format(list_headers).split("\n")
    else:
        headers=[
          num_load_nodes,
          num_load_uniformly,
          num_trapezoidally_load,
          num_concentrated_loads,
          num_temperature_loads,
          num_displacements
                ]
    #----------------------------
    # WRITE - LOADED  NODES
    wr(headers[0])
    data_list=[]
    if use_comments:
        data_list=[["#node ","x-load ","y-load ","z-load ","x-mom ","y-mom ","z-mom"]]
    for x in data_load_nodes:
        data_list.append(x)
    if num_load_nodes:
        wr(data_format(data_list))

    #----------------------------
    # WRITE - UNIFORMLY DISTRIBUTED LOADS
    if num_load_nodes and use_comments:wr("")
    wr(headers[1])
    data_list=[]
    if use_comments:
        data_list=[["#element ","x-dist-load ","y-dist-load ","z-dist-load "]]
    for x in data_load_uniformly:
        data_list.append(x)
    if num_load_uniformly:
        wr(data_format(data_list))

    #----------------------------
    # WRITE - TRAPEZOIDALLY DISTRIBUTED LOADS
    if num_load_uniformly and use_comments:wr("")
    wr(headers[2])
    data_list=[]
    if use_comments:
        data_list=[["#element ","start ","end  ","start-load ","end-load "]]
    #........................
    first=True
    for x in data_trapezoidally_load:
        #------
        if first: first = False
        else:
            if use_comments:
                data_list.append(["#---","---","---","---","---"])
        #-----
        line=[x[0],x[1],x[2],x[3],x[4]]
        if use_comments:
            line.append("# x axis - el."+str(x[0]))
        data_list.append(line[:])    
        line=["",x[5],x[6],x[7],x[8]]
        if use_comments:
            line.append("# y axis - el."+str(x[0]))
        data_list.append(line[:])    
        line=["",x[9],x[10],x[11],x[12]]
        if use_comments:
            line.append("# z axis - el."+str(x[0]))
        data_list.append(line[:])    


    #........................
    if num_trapezoidally_load:
        wr(data_format(data_list))


    #----------------------------
    # WRITE - CONCENTRATED INTERIOR POINT LOADS
    if num_trapezoidally_load and use_comments:wr("")
    wr(headers[3])
    data_list=[]
    if use_comments:
        data_list=[["#element ","x-load ","y-load ","z-load ","x-location  "]]
    for x in data_concentrated_loads:
        data_list.append(x)
    if num_concentrated_loads:
        wr(data_format(data_list))

 

    #----------------------------
    # WRITE - TEMPERATURE LOADS
    if num_concentrated_loads and use_comments:wr("")
    wr(headers[4])
    data_list=[]
    if use_comments:
        data_list=[["#element ","coef. ","y-depth ","z-depth ","delta-Ty+ ","delta-Ty- ","delta-Tz+ ","delta-Tz+ "]]
    for x in data_temperature_loads:
        data_list.append(x)
    if num_temperature_loads:
        wr(data_format(data_list))

    #----------------------------
    # WRITE - DISPLACEMENTS
    if num_temperature_loads and use_comments:wr("")
    wr(headers[5])
    data_list=[]
    if use_comments:
        data_list=[["#node ","x-displ ","y-displ ","x-rotation ","y-rotation ","z-rotation "]]
    for x in data_displacements:
        data_list.append(x)
    if num_displacements:
        wr(data_format(data_list))

    #----------------------------

    if use_comments:
        wr("")
        wr("# end "+text)
        wr("")
        pass
    
#-----------------------------------------------------

def write_load_cases(wr_function,var_object):
    #----------------
    wr=wr_function
    obj=var_object
    use_comments=var_object.use_comments
    #----------------
    list_load_cases=obj.list_load_cases[:]
    last_case=obj.current_load_case
    if last_case.is_valid_load_case():
        list_load_cases.append(last_case)
    num_load_cases=len(list_load_cases)
    #----------------
    if use_comments:
        wr("")
        wr(str(num_load_cases)+" # number of load  cases")
        wr("# BEGIN LOAD CASES")
        wr("")
    else:
        wr(num_load_cases)
    #---------------
    var=0
    num=num_load_cases
    for obj_l_case in list_load_cases:
        var+=1
        write_a_load_case(obj_l_case,var,num,use_comments,wr)

    #---------------
    if  use_comments:
        wr("# END LOAD CASES")






