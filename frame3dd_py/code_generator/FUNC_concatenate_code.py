# code  generator for frame3dd syntax input file
# by Edwin Saul PM

def concatenate(obj):

    class class_code:
        def __init__(self)      : self.code_string=""
        def get_code(self)      : return self.code_string
        def write(self,element) :
            self.code_string+=str(element)+"\n"
    obj_code=class_code() ; wr=obj_code.write   

    #----------------------------
    use_comments=obj.use_comments
    wr(obj.structure_name)  #name of the model
    if use_comments: wr(88)
        



    #----------------------------

    return obj_code.get_code()


