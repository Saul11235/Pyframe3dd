# frame3dd_py  writed by:  Edwin Saul PM 

import pyframe3dd

def contents(parent):
    response=[]
    for x in dir(parent):
        try:
            if x[0]!="_":response.append(x)
        except: pass
    return response    

for x in contents(pyframe3dd):
    obj=getattr(pyframe3dd,x)
    print("\n"+x+"\t\t"+str(type(obj))+"\n")
    if type(obj)==type:
        for xx in contents(obj):
            cont=getattr(obj,xx)
            print("  "+xx+"\t"+str(type(cont)))
    print("\n")

    





