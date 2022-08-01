# code  generator for frame3dd syntax input file
# by Edwin Saul PM

class CONFIG_input_source:

    def include_shear_effects(self):
        self.__shear_effects=1

    def include_geometry_stiffness(self):
        self:__geometry_stiffness=1

