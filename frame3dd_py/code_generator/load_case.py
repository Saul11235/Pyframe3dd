# code  generator for frame3dd syntax input file
# by Edwin Saul PM

def is_num(var):
    if type(var)==int or type(var)==float: return True   
    else: return False

def list_is_num(list_var):
    cont=0
    for x in list_var:
        if  is_num(x):cont+=1
    if len(list_var)==cont:return True
    else: return False

#------------------------------

class  set_load_case:

    def __is_element(self,number_element):
        if  type(number_element)==int:
            if  self.number_of_elements>=number_element and number_element>0:
                return True 
            else:  return False
        else: return False

    def __is_node(self,number_node):
        if  type(number_element)==int:
            if  self.number_of_nodes>=number_node and number_node>0:
                return True 
            else:  return False
        else: return False

    #--------------------------

    def new_load_case(self):
        pass

    def gravity(self,gx,gy,gz):
        if list_is_num([gx,gy,gz]):
            self.current_load_case.set_gravity(gx,gy,gz)
        else:
            return False


 
