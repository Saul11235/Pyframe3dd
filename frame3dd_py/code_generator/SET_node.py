# code  generator for frame3dd syntax input file
# by Edwin Saul PM

#try:    from .DEF_node import class_node
#except: from DEF_node  import class_node


class  set_node:

    def node(self,x,y,z,radius):
        #obj_node   =  class_node(x,y,z,radius)
        #self.list_nodes.append(obj_node)
        self.number_of_nodes += 1
        return self.number_of_nodes


    
