
try:    from .__all_classes__ import __all_classes__
except: from __all_classes__  import __all_classes__

from os import system

exceptions=[
        ]
requeriments=__all_classes__(exceptions)

class run_code_class(requeriments):

    #----------------------------------

    def __init__(self,code):
        # input
        self.__command_frame3dd="frame3dd"
        self.__code=""
        try:self.__code=str(code)
        except:pass
        self.__inputName ="input.3dd"
        self.__outputName="output.3dd"

    #----------------------------------

    def set_command_frame3dd(self,command):
        if type(command)==str:
            self.__command_frame3dd=command
            return True
        else:return False 

    #----------------------------------

    def set_code(self,code):
        if type(code)==str:
            self.__code=code
            return True
        else:return False 

    #----------------------------------

    def run(self):
        f=open(self.__inputName,"w")
        f.write(self.__code)
        f.close()
        #---creating code to run program---
        to_run=self.__command_frame3dd+" -i "
        to_run+=self.__inputName
        to_run+=" -o "+self.__outputName



        #----------------------------------
        #runnig program
        system(to_run)









