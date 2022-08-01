# code  generator for frame3dd syntax input file
# all name variables are based on frame3dd doc 
# by Edwin Saul PM

class node:

    def  __init__(self,x,y,z,radius):
        #coordinates - radius
        self.x      = x
        self.y      = y
        self.z      = z
        self.radius = radius
        #reaction data -  0 free / 1 fixed
        self.Rx     = 0  #displacement
        self.Ry     = 0
        self.Rz     = 0
        self.Rxx    = 0  #rotation
        self.Ryy    = 0
        self.Rzz    = 0

    def set_reactions(self,Rx,Ry,Rz,Rxx,Ryy,Rzz):
        self.Rx     = Rx
        self.Ry     = Ry
        self.Rz     = Rz
        self.Rxx    = Rxx
        self.Ryy    = Ryy
        self.Rzz    = Rzz

