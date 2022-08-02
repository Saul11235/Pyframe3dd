# code  generator for frame3dd syntax input file
# by Edwin Saul PM

class set_element:

    def element(self,n1,n2,Ax,Asy,Asz,Jx,Iy,Iz,E,G,roll,dens):
        # n1     : node origin
        # n2     : node end
        # Ax     : section  area - perpendicular to x axis
        # Asy    : shear area (y direction)
        # Asz    : shear area (y direction)
        # Jx     : torsional momment of inertia
        # Iy     : moment of inertia relative to y axis 
        # Iz     : moment of inertia relative to z axis
        # E      : modulus of elasticy
        # G      : shear modulus  of elasticy
        # roll   : rotation  section
        # density: density   section

        def is_numeric(value):
            if type(value)==int or type(value)==float:
                return   True
            else: return False

        def is_numeric_list(list_values):
            number_true_values=0
            for value in list_values: 
                if is_numeric(value):
                    number_true_values+=1
            if len(list_values)==number_true_values: 
                return   True
            else: return False

        def node_valid(number):
            if type(number)==int:
                if (number>0)and(number<=self.number_of_nodes):
                    return   True
                else: return False
            else: return False

        arguments=[n1,n2,Ax,Asy,Asz,Jx,Iy,Iz,E,G,roll,dens]

        valid_nodes     = node_valid(n1) and node_valid(n2)
        valid_arguments = is_numeric_list(arguments)

        if valid_nodes and  valid_arguments:
            #new element
            obj_element = self.class_element(*tuple(arguments))
            self.list_elements.append(obj_element)
            self.number_of_elements += 1
            return self.number_of_elements
        else: return False


