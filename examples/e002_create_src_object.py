# frame3dd_py  writed by:  Edwin Saul PM 

from frame3dd_py import input_code

obj=input_code()
obj.comments()  #view the  comments in the code generated

#  node( x,   y,   z,   radius)
obj.node(0,   0,   50,  0) # node 1
obj.node(100, 0,   0,   0) # node 2
obj.node(0,   100, 0,   0) # node 3

# restriction node Nnode rx ry rz rxx ryy rzz
obj.restriction_node(2,   1, 1, 1, 1,  1,  1)
obj.restriction_node(1,   1, 1, 1, 1,  1,  1)
# 0 free - 1  fixed

# element data
#           n1  n2  Ax   Asy  Asz  Jx   Iy  Iz  E  G  roll dens
obj.element(1,  2,  9,   8,   7.1, 6,   5,  4,  3, 2, 2.1, 2.1)
obj.element(2,  3,  9,   8.1, 7,   6,   5,  4,  3, 2, 2.1, 2.1)
obj.element(1,  3,  9.1, 8,   7,   6,   5,  4,  3, 2, 2.1, 2.1)

# set gravity on current  load case
#           gx  gy  gz
obj.gravity(0,  0,  -9.81)

print(obj.get_code())


