from tkinter import * 

root = Tk()
root.title('Covidayudas/Persona')
root.geometry('323x400')

my_canvas = Canvas(root, width=323, height=400)
my_canvas.pack(fill="both", expand=True)


#Boxes
n_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
a_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
ingreso_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
dni_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
n_entry.insert(0, "Nombre")
a_entry.insert(0, "Apellido")
ingreso_entry.insert(0, "Ingreso Anual")
dni_entry.insert(0, "DNI" )
#ad boxes to canvas
n_window = my_canvas.create_window(34, 50, anchor="nw", window=n_entry)
a_window = my_canvas.create_window(34, 100, anchor="nw", window=a_entry)
ing_entry = my_canvas.create_window(34, 150, anchor="nw", window=ingreso_entry)
dni_window = my_canvas.create_window(34, 200, anchor="nw", window=dni_entry)

#button
send_btn = Button(root, text= "Send", font=("Helvetica", 20 ), width=15, fg="#336d92")
send_btn_window = my_canvas.create_window(34, 300, anchor="nw", window=send_btn)

def entry_clear(e): 
    
    if a_entry.get() == 'Nombre' or n_entry.get() == 'Apellido' or  ingreso_entry.get() == 'Ingreso Anual' or dni_entry.get() == 'DNI' : 
        a_entry.delete(0, END)
        n_entry.delete(0, END)
        dni_entry.delete(0, END)
        ingreso_entry.delete(0,END)


a_entry.bind("<Button-1>", entry_clear)
n_entry.bind("<Button-1>", entry_clear)
ingreso_entry.bind("<Button-1>", entry_clear)
dni_entry.bind("<Button-1>", entry_clear)


root.mainloop()