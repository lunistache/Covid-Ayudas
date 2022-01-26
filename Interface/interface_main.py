from tkinter import * 
import sys
import os

root = Tk()
root.title('Covidayudas')
root.geometry('323x200')

my_canvas = Canvas(root, width=323, height=200)
my_canvas.pack(fill="both", expand=True)

def run_emp():
    os.system('interface_empresa.py')

def run_per(): 
    os.system('interface_persona.py')



#buttons 
  
empresa_btn = Button(root, text= "Empresa", font=("Helvetica", 20 ), width=15, fg="#336d92", command=run_emp)
empresa_btn_window = my_canvas.create_window(34, 25, anchor="nw", window=empresa_btn)

persona_btn = Button(root, text= "Persona", font=("Helvetica", 20 ), width=15, fg="#336d92", command=run_per)
persona_btn_window = my_canvas.create_window(34, 100, anchor="nw", window=persona_btn)







root.mainloop()