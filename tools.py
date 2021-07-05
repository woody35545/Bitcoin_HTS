def p(arg):
    print(arg)
def listp (list,listname):
    for i in range (len(list)):
        p(f"{listname}[{i}]: {list[i]}")


def get_fileContents(filename):
    f = open(filename,'r', encoding = 'UTF8')
    res_str = ""
    buffer = ""
    while True:
        buffer = f.readline()
        if not buffer:
            break
        res_str += buffer
    return res_str

def textReplace(input_string,old_text, text_to_change):
    return str(input_string).replace(old_text,text_to_change)

def gmf_button_clicked (gui_commponent_name, function_name_to_apply):
    p("self."+ gui_commponent_name +".clicked.connect(self." + function_name_to_apply + ")")
def gmf_textEdit_setText(gui_commponent_name,inputstr):
    p("self."+ gui_commponent_name +".setText(\"" + str(inputstr) + "\")")

