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



