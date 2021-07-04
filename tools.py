def gmf_button_clicked (gui_commponent_name, function_name_to_apply):
    print("self."+ gui_commponent_name +".clicked.connect(self." + function_name_to_apply + ")")
def gmf_textEdit_setText(gui_commponent_name,inputstr):
    print("self."+ gui_commponent_name +".setText(\"" + str(inputstr) + "\")")

