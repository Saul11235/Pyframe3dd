
# code for run example
import p01_code_example
code=p01_code_example.obj.get_code()

#--------------------------------

#running app from object
from pyframe3dd import run_code

#-------------------------------
#

run=run_code(code)
run.run()

print("example loaded!")

