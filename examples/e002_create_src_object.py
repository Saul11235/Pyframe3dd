# frame3dd_py  writed by:  Edwin Saul PM 

from pyframe3dd import input_code

obj=input_code()
obj.comments()  #view the  comments in the code generated

#  node( x,   y,   z,   radius)
obj.node(0,   0,   50,  0) # node 1
obj.node(100, 0,   0,   0) # node 2
obj.node(0,   100, 0,   0) # node 3

# restriction node Nnode rx ry rz rxx ryy rzz
obj.restriction_node(2,   1, 1, 1, 1,  1,  1)
obj.restriction_node(1,   1, 1, 1, 1,  1,  1)
obj.restriction_node(3,   0, 0, 0, 0,  0,  0)
# 0 free - 1  fixed

# element data
#           n1  n2  Ax   Asy  Asz  Jx   Iy  Iz  E  G  roll dens
obj.element(1,  2,  9,   8,   7.1, 6,   5,  4,  3, 2, 2.1, 2.1)
obj.element(2,  3,  9,   8.1, 7,   6,   5,  4,  3, 2, 2.1, 2.1)
obj.element(1,  3,  9.1, 8,   7,   6,   5,  4,  3, 2, 2.1, 2.1)

# first load  case  default

# set gravity on current  load case
#           gx  gy  gz
obj.gravity(10,  1.30,  -9.81)

# set load on node 
#             node  xload  yload  zload  xmom   ymom   zmom
obj.load_node(2,    11,    12,    13,    14,    15,    16)
obj.load_node(1,    10,    12,    13,    14,    15,    16)

# load distributed on element
#                    element   x--load   y--load   z--load
obj.load_dist_element(1,       20,       30,       40)
obj.load_dist_element(2,       22,       32,       42)


# load trapezoidally distributed element loads
obj.load_trapezoidally()

#obj.new_load_case()


#obj.gravity(1,2,3)



print(obj.get_code())

a=open("generated.3dd","w")
a.write(obj.get_code())
a.close()

#from os import system

#system("frame3dd -i generated.3dd  -o end.out -w matrix.out")






