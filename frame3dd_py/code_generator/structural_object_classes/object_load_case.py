# code  generator for frame3dd syntax input file
# all name variables are based on frame3dd doc 
# by Edwin Saul PM

class class_load_case:

    def __init__(self):

        # gravitational aceleration 
        self.gX  = 0
        self.gY  = 0
        self.gZ  = 0

        # load on nodes
        # [ #node  x-load  y-load  z-load  x-mom  y-mom  z-mom ]
        self.load_nodes                  = []

        # uniformly distributed  element loads
        # [ #element x-unfrm-load y-unfrm-load z-unfrm-load ]
        self.load_uniformly              = []

        # trapezoidally distributed element loads
        # [ #element  xx1  xx2  Wx1  Wx2 - xy1  xy2 Wy1 Wy2 - xz1 xz2 Wz1 Wz2 ]
        self.trapezoidally_load          = []

        # concentrated interior point loads
        # [ #element  x-load y-load z-load x-loc  ]
        self.concentrated_interior_loads = []

        # frame elements  with  temperature changes
        # [ #element  coef  y-depth  z-depth  deltaTy+  deltaTy- deltaTz+ deltaTz- ]
        self.temperature_loads           = []

        # prescribed displacements
        # [#node   x-disp  y-disp z-disp x-rot y-rot z-rot ]
        self.prescribed_displacements    = []
        
    def set_gravity(self,gx,gy,gz):
        self.gX = gx
        self.gY = gy
        self.gZ = gz

    def set_load_nodes(self,node,xl,yl,zl,xm,ym,zm):
        list_var=[node,xl,yl,zl,xm,ym,zm]
        self.load_nodes.append(list_var)

    def set_load_uniformly(self,element,xu,yu,zu):
        list_var=[element,xu,yu,zu]
        self.load_uniformly.append(list_var)

    def set_trapezoidally(self,element,xx1,xx2,Wx1,Wx2,   xy1,xy2,Wy1,Wy2  ,xz1,xz2,Wz1,Wz2):
        list_var=[element,xx1,xx2,Wx1,Wx2,   xy1,xy2,Wy1,Wy2  ,xz1,xz2,Wz1,Wz2]
        self.trapezoidally_load.append(list_var)
        
    def set_concentrated(self,element,xload,yload,zload,xlocation):
        list_var=[element,xload,yload,zload,xlocation]
        self.concentrated_interior_loads.append(list_var)

    def set_temperature_load(self,element,coef, yd, zd, deltaTypositive, deltaTynegative, deltaTzpositive, deltaTznegative):
        list_var=[element,coef, yd, zd, deltaTypositive, deltaTynegative, deltaTzpositive, deltaTznegative]
        self.temperature_loads.append(list_var)

    def set_displacements(self,node,xd,yd,zd,xr,yr,zr):
        list_var=[node,xd,yd,zd,xr,yr,zr]
        self.prescribed_displacements.append(list_var)

    def is_valid_load_case(self):

        gravity=False
        if self.gX!=0 or self.gY!=0 or self.gZ!=0:
            gravity=True

        #--------------------------

        have_loads       = False    
        if len(self.load_nodes):
            have_loads   = True

        have_loads_u     = False
        if len(self.load_uniformly): 
            have_loads_u = True

        have_loads_t     = False
        if len(self.trapezoidally_load):
            have_loads_t = True

        have_loads_c     = False
        if len(self.concentrated_interior_loads):
            have_loads_c = True

        have_loads_tmp   = False
        if len(self.temperature_loads):
            have_loads_tmp=True

        have_desplacements=False
        if len(self.prescribed_displacements):
            have_desplacements = True

        #------------------

        loads=False
        if have_loads or have_loads_u or have_loads_t or have_loads_c or have_loads_tmp or have_desplacements:
            loads=True

        #------------------
        if loads or gravity:
            return True
        else:
            return  False

