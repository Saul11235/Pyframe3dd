#
# __all_classes__ 
#  in  current path
#

from   platform        import  system
from   os              import  path
from   os.path         import  isdir,isfile
import importlib.util
import pathlib

slash = "" 
if system()=="Windows": slash = "\\"
else                  : slash = "/"

class module_scanner:

    def read_module(self,module_name,*args):

        #  test ok -  py 3.10
        # ref: https://www.delftstack.com/es/howto/python/import-python-file-from-path/

        namePyFile = ""; isPythonFile = False
        if len(args):
            namePyFile = args[0]; isPythonFile = True 

        name = str(module_name)
        path = str(self.directory) 

        if isPythonFile: 
            MODULE_PATH = path+slash+namePyFile
            MODULE_NAME = name
            spec        = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
            modulevar   = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulevar)
            return modulevar 
        else:
            MODULE_PATH = path+slash+name+slash+"__init__.py"
            MODULE_NAME = name
            spec        = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
            modulevar   = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulevar)
            return modulevar

    def  __init__(self,var_list_exceptions_input):
        
        self.directory=path.dirname(path.abspath(__file__))
        self.classes        = []  
        self.list_py_files  = []  
        self.list_modules   = []  
        self.exception_list = []
        self.module_objects = []   

        for x in var_list_exceptions_input:
            full_path=self.directory+slash+str(x)
            self.exception_list.append(full_path)

        self.identify_files_modules() 

        for x in self.list_py_files:  self.inspect_file(x)
        for x in self.list_modules:   self.inspect_module(x) 
        for x in self.module_objects: self.inspect_classes_on_module(x)

    def inspect_classes_on_module(self,module):
        var_list = dir(module)
        for name in var_list:
            var_object = getattr(module,name)
            if type(var_object)==type: self.set_new_class(var_object)

    def add_module(self,module): self.module_objects.append(module)

    def get_name_file(self,var_path):  
        str0       = str(var_path)
        str1       = str0[0:len(str0)-3] # delete ".py"
        str2       = str1[::-1]
        acumulator = "" 
        separator  = slash;var_pass=True
        for x in str2:
            if   var_pass and x == separator: var_pass=False
            elif var_pass and x != separator: acumulator+=x
        final=acumulator[::-1]
        return final # return "name" from "...\name.py"

    def get_module_name(self,var_path):
        str1       = str(var_path)
        str2       = str1[::-1]
        acumulator = ""
        separator  = slash;var_pass=True
        for x in str2:
            if   var_pass and x == separator: var_pass=False
            elif var_pass and x != separator: acumulator=acumulator+x
        final=acumulator[::-1]
        return final #d return "name" from ..../name

    def inspect_file(self,var_path_file):
        name   = self.get_name_file(var_path_file)
        module = self.read_module(name,name+".py")
        self.add_module(module)

    def inspect_module(self,var_pathmodule):
        name   = self.get_module_name(var_pathmodule)
        module = self.read_module(name)
        self.add_module(module)

    def set_new_class(self,var_class):
        self.classes.append(var_class)

    def is_exception(self,registry):
        var_path = str(registry)
        try    :
            self.exception_list.index(var_path)
            return True
        except : return False

    def ends_dot_py(self,directory):
        var_path = str(directory)
        if len(var_path)>3:
            extension = var_path[len(var_path)-3:]
            if extension == ".py": return True
            else:                  return False
        else: return False

    def is_module(self,var_path):
        name         = str(var_path)+slash+"__init__.py"
        no_is_module = False 
        for x in var_path.iterdir():
            if  not(x.is_dir()):
                texto=str(x)
                if  texto==name:
                    no_is_module=True
        return no_is_module

    def identify_files_modules(self):
        directory = pathlib.Path(self.directory)
        for x in directory.iterdir():
            if   self.is_exception(x):pass
            elif x.is_dir():
                if  self.is_module(x):
                    self.list_modules.append(x)
            else:
                if  self.ends_dot_py(x):
                    self.list_py_files.append(x)

    def var_tuple_classes(self):
        return tuple(self.classes)

#---------------------------------------

def __all_classes__(*var_list_exceptions_in_init):
    var_list_exceptions=["__init__.py","__all_classes__.py","__pycache__"]

    for x in var_list_exceptions_in_init:
        if  type(x)==str:
            var_list_exceptions.append(x)
        elif type(x)==list or type(x)==tuple:
            for xx in x:
                if  type(xx)==str:
                    var_list_exceptions.append(xx)

    scanner=module_scanner(var_list_exceptions)
    var_tuple=scanner.var_tuple_classes()
    class acumulator_class(*var_tuple):pass    
    return acumulator_class
