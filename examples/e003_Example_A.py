# recreation example A oficial frame 3dd 
# frame3dd_py  writed by:  Edwin Saul PM 

from pyframe3dd import input_code

obj=input_code()
obj.comments()  #view the  comments in the code generated

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





print(obj.get_code())





