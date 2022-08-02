# code  generator for frame3dd syntax input file
# by Edwin Saul PM

class CONFIG_input_source:

    def set_name(self,name):
        self.structure_name=str(name)

    def no_comments(self):
        self.var_use_comments=True

    def include_shear_effects(self):
        self.shear_effects=1

    def include_geometry_stiffness(self):
        self:geometry_stiffness=1

