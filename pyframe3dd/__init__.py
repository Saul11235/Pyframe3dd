#
#  python package for structural  modeling 
#  using the frame3dd  program
#
#  frame3dd program project page:
#  http://frame3dd.sourceforge.net/
#
#  frame3dd_py package
#  Edwin Saul PM
#

try:    from .__code_generator import input_code_class  as __input
except: from __code_generator  import input_code_class  as __input

class input_code(__input):
    pass


try:    from .__run_code import run_code_class as __run
except: from __run_code  import run_code_class as __run

class run_code(__run):
    pass
#---------------------------------------------------




