# recreation example A oficial frame 3dd 
# frame3dd_py  writed by:  Edwin Saul PM 

from pyframe3dd import input_code

obj=input_code()
obj.comments()  #view the  comments in the code generated

obj.set_name("Example A: linear static analysis of a 2D truss with support settlement (kips,in)")

#---------------------------------
#  node( x,      y,      z,      radius)
#        inches  inches  inches  inches
#---------------------------------
obj.node(0,      0,      0,      0) # node 1
obj.node(120,    0,      0,      0) # node 2
obj.node(240,    0,      0,      0) # node 3
obj.node(360,    0,      0,      0) # node 4
obj.node(480,    0,      0,      0) # node 5
obj.node(600,    0,      0,      0) # node 6
obj.node(0,      120,    0,      0) # node 7
obj.node(120,    120,    0,      0) # node 8
obj.node(240,    120,    0,      0) # node 9
obj.node(360,    120,    0,      0) # node 10
obj.node(480,    120,    0,      0) # node 11
obj.node(600,    120,    0,      0) # node 12

# 0 Free / 1 Fixed
#-----------------------------------------------
# restriction node Nnode rx ry rz   rxx ryy rzz
#-----------------------------------------------
obj.restriction_node(1,   1, 1, 1,   1,  1,  0)
obj.restriction_node(2,   0, 0, 1,   1,  1,  0)
obj.restriction_node(3,   0, 0, 1,   1,  1,  0)
obj.restriction_node(4,   0, 0, 1,   1,  1,  0)
obj.restriction_node(5,   0, 0, 1,   1,  1,  0)
obj.restriction_node(6,   0, 0, 1,   1,  1,  0)
obj.restriction_node(7,   0, 1, 1,   1,  1,  0)
obj.restriction_node(8,   1, 0, 1,   1,  1,  0)
obj.restriction_node(9,   0, 0, 1,   1,  1,  0)
obj.restriction_node(10,  0, 0, 1,   1,  1,  0)
obj.restriction_node(11,  0, 0, 1,   1,  1,  0)
obj.restriction_node(12,  0, 0, 1,   1,  1,  0)


# Material Section properties
Ax  = 10      # Section Area  -  inches^2
Asy = 1       # Shear Area y  -  inches^2
Asz = 1       # Shear Area z  -  inches^2
Jx  = 1       # Torsional inertia momment  - inches^4
Iy  = 1       # inertia mommet axis y      - inches^4
Iz  = 1       # inertia mommet axis z      - inches^4
E   = 2900    # modulus of elasticy        - ksi
G   = 11500   # Shear modulus of elasticy  - ksi
roll= 0       # roll angle section         - degress
dens= 7.33e-7 # density  kip/inch^3/g

#----------------------------------------------------------------------
# new element(n1 ,n2 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens)
#----------------------------------------------------------------------
obj.element  (1  ,2  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 1
obj.element  (2  ,3  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 2
obj.element  (3  ,4  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 3
obj.element  (4  ,5  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 4
obj.element  (5  ,6  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 5
obj.element  (6  ,7  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 6
obj.element  (1  ,8  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 7
obj.element  (2  ,8  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 8
obj.element  (2  ,9  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 9
obj.element  (3  ,9  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 10
obj.element  (4  ,9  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 11
obj.element  (4  ,10 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 12
obj.element  (4  ,11 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 13
obj.element  (5  ,11 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 14
obj.element  (6  ,11 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 15
obj.element  (6  ,12 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 16
obj.element  (7  ,12 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 17
obj.element  (8  ,9  ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 18
obj.element  (9  ,10 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 19
obj.element  (10 ,11 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 20
obj.element  (11 ,12 ,Ax ,Asy ,Asz ,Jx ,Iy ,Iz ,E ,G ,roll ,dens) #elem 21

# DEFAULT: no shear deformation
# DEFAULT: no geometric stiffness

# funtion to set exagerate mesh 50

# DEFAULT: zoom scale for 3d plot=1
# DEFAULT: calculus internal forces skiped


#----------------------------------------------
#            LOAD CASE  1
#----------------------------------------------

# load_node   node  xload  yload  zload  xmom   ymom   zmom
obj.load_node(2,    0,    -10,    0,     0,     0,     0)
obj.load_node(3,    0,    -20,    0,     0,     0,     0)
obj.load_node(4,    0,    -20,    0,     0,     0,     0)
obj.load_node(5,    0,    -10,    0,     0,     0,     0)
obj.load_node(6,    0,    -20,    0,     0,     0,     0)




#----------------------------------------------
#            LOAD CASE  2
#----------------------------------------------
obj.new_load_case() 






print(obj.get_code())





