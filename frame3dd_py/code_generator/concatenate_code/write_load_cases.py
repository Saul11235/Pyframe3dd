# code  generator for frame3dd syntax input file
# by Edwin Saul PM


try:    from .data_to_string import data_format
except: from data_to_string  import data_format



def write_a_load_case(obj,number,total,use_comments,wr):

    text=""
    text2="case "+str(number)
    if use_comments:
        text=" load case "+str(number)+" of "+str(total)

    if use_comments:
        wr("# begin "+text)
    #----------------------------
    # WRITE - GRAVITY 
    line=[]
    if use_comments:
        wr("")
        line.append(["#gx  ","gy  ","gz   ","  gravity "+text2])
    line.append([obj.gX , obj.gY ,  obj.gZ])   
    wr(data_format(line))
    if use_comments: wr("")

    #----------------------------
    # WRITE - LOADED  NODES


    #----------------------------
    # WRITE - UNIFORMLY DISTRIBUTED LOADS

    #----------------------------
    # WRITE - TRAPEZOIDALLY DISTRIBUTED LOADS

    #----------------------------
    # WRITE - CONCENTRATED INTERIOR POINT LOADS

    #----------------------------
    # WRITE - TEMPERATURE LOADS

    #----------------------------
    # WRITE - DISPLACEMENTS

    #----------------------------

    if use_comments:
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
    list_load_cases=obj.list_load_cases
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






