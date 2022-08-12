# code  generator for frame3dd syntax input file
# by Edwin Saul PM

class details_code:

    def  num_nodes_with_reactions(self):
        num_reactions=0
        for node in self.list_nodes:
            if  not(node.is_free()):num_reactions+=1
        return num_reactions

