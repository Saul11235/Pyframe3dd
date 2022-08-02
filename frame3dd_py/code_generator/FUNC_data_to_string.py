# code  generator for frame3dd syntax input file
# by Edwin Saul PM

def data_format(object_list):
    
    list_string=[]
    for line_list in object_list:
        element_str  = []
        for element in line_list: element_str.append(str(element))
        list_string.append(element_str[:])
    
    n_columns=0
    for line_list in list_string:
        n_columns    = max(n_columns,len(line_list))

    size_cell_by_column=[0]*n_columns
    for line_list in list_string:
        var=0
        for element in line_list:
            len_col  = size_cell_by_column[var]
            len_elem = len(element)
            new_len  = max(len_col,len_elem)
            size_cell_by_column[var]=new_len
            var+=1

    def write_line(line_list,textvar):
        var=0; final = len(line_list)
        for element in line_list:
            textvar+=element
            len_column=size_cell_by_column[var]
            var+=1
            nspaces=1+len_column-len(element)
            if not(final<=var): textvar+=" "*nspaces
        return textvar

    text="";first=True
    for line_list in list_string:
        if first : first=False
        else     : text+="\n"
        text  = write_line(line_list,text)
    return text
        

