# code  generator for frame3dd syntax input file
# by Edwin Saul PM


class  set_node:


    def node(self,x,y,z,radius):
        obj_node   =  self.class_node(x,y,z,radius)
        self.list_nodes.append(obj_node)
        self.number_of_nodes += 1
        return self.number_of_nodes


    def restriction_node(self,Nnode,rx,ry,rz,rxx,ryy,rzz):
        # restrictions 1 fixed /  0 free
        def get_restriction_by_obj(var):
            try: [0,0.0,False].index(var);return 0
            except: return 1
        #-------    
        list_restrictions=[]
        #-------
        list_restrictions.append(get_restriction_by_obj(rx))
        list_restrictions.append(get_restriction_by_obj(ry))
        list_restrictions.append(get_restriction_by_obj(rz))
        list_restrictions.append(get_restriction_by_obj(rxx))
        list_restrictions.append(get_restriction_by_obj(ryy))
        list_restrictions.append(get_restriction_by_obj(rzz))
        #-------
        # time of hadouken code!
        if type(Nnode)==int:
            if (Nnode>0) and (Nnode<=self.number_of_nodes):
                obj_node=self.list_nodes[Nnode-1]
                tuple_rstr=tuple(list_restrictions)
                if tuple_rstr==tuple([0,0,0,0,0,0]):
                    return False
                else:
                    obj_node.set_restrictions(*tuple_rstr)
                    return  True
            else:return False
        return False


