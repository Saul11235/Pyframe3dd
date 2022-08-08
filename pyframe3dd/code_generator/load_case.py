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

    def __is_element(self,number):
        print(number)
        if  type(number)==int:
            if  self.number_of_elements>=number and number>0:
                return True 
            else:  return False
        else: return False

    #--------------------------

    def __is_node(self,number_node):
        if  type(number_node)==int:
            if  self.number_of_nodes>=number_node and number_node>0:
                return True 
            else:  return False
        else: return False

    #--------------------------

    def new_load_case(self):
        if self.current_load_case.is_valid_load_case():
            if self.number_of_load_cases<30:
                self.number_of_load_cases+=1
                self.list_load_cases.append(self.current_load_case)
                self.current_load_case =self.class_load_case()
                return self.number_of_load_cases
            else: return False
        else: return False

    #---------------------------    

    def gravity(self,gx,gy,gz):
        if list_is_num([gx,gy,gz]):
            self.current_load_case.set_gravity(gx,gy,gz)
            return True
        else:
            return False

    #---------------------------    

    def load_node(self,node,xload,yload,zload,xmom,ymom,zmom):
        list_load=[node,xload,yload,zload,xmom,ymom,zmom]
        if list_is_num(list_load):
            if self.__is_node(node):
                self.current_load_case.set_load_nodes(*tuple(list_load))
                return True
            else:
                return False
        else: return False

    #---------------------------    

    def load_dist_element(self,element,load_x,load_y,load_z):
        list_load=[element,load_x,load_y,load_z]
        if list_is_num(list_load):
            if self.__is_element(element):
                self.current_load_case.set_load_uniformly(*tuple(list_load))
                return True
            else:
                return False
        else:
            return False

    #---------------------------

    def load_trapezoidally(self):
        pass






