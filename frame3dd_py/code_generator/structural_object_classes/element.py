# code  generator for frame3dd syntax input file
# all name variables are based on frame3dd doc 
# by Edwin Saul PM

class element:

    def __init__(self,n1,n2,Ax,Asy,Asz,Jx,Iy,Iz,E,G,roll,density):
        self.n1       = n1   # node origin
        self.n2       = n2   # node end
        self.Ax       = Ax   # section  area - perpendicular to x axis
        # SHEAR EFFECTS
        self.Asy      = Asy  # shear area (y direction)
        self.Asz      = Asz  # shear area (y direction)
        # Note.- see Timoshenko beam theory
        # AEH Love A Treatise on the Mathematical Theory of Elasticity
        self.Jx       = Jx   # torsional momment of inertia
        self.Iy       = Iy   # moment of inertia relative to y axis 
        self.Iz       = Iz   # moment of inertia relative to z axis
        # mechanical factors
        self.E        = E       # modulus of elasticy
        self.G        = G       # shear modulus  of elasticy
        self.roll     = roll    # rotation  section
        self.density  = density # density   section



        
         


