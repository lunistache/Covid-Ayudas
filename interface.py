from tkinter import * 

root = Tk()
root.title('Covidayudas')
root.geometry('323x500')

my_canvas = Canvas(root, width=323, height=500)
my_canvas.pack(fill="both", expand=True)


#Boxes
n_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
a_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
cif_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
cnae_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
dni_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
n_entry.insert(0, "Nombre")
a_entry.insert(0, "Apellido")
cif_entry.insert(0, "CIF")
cnae_entry.insert(0, "CNAE")
dni_entry.insert(0, "DNI" )
#ad boxes to canvas
n_window = my_canvas.create_window(34, 100, anchor="nw", window=n_entry)
a_window = my_canvas.create_window(34, 150, anchor="nw", window=a_entry)
cif_window = my_canvas.create_window(34, 200, anchor="nw", window=cif_entry)
cnae_window = my_canvas.create_window(34, 250, anchor="nw", window=cnae_entry)
dni_window = my_canvas.create_window(34, 300, anchor="nw", window=dni_entry)

#button
send_btn = Button(root, text= "Send", font=("Helvetica", 20 ), width=15, fg="#336d92")
send_btn_window = my_canvas.create_window(34, 370, anchor="nw", window=send_btn)

def entry_clear(e): 
    
    if a_entry.get() == 'Nombre' or n_entry.get() == 'Apellido' or cif_entry.get() == 'CIF' or cnae_entry.get() == 'CNAE' or dni_entry.get() == 'DNI' : 
        a_entry.delete(0, END)
        n_entry.delete(0, END)
        cif_entry.delete(0, END)
        cnae_entry.delete(0, END)
        dni_entry.delete(0, END)


a_entry.bind("<Button-1>", entry_clear)
n_entry.bind("<Button-1>", entry_clear)
cif_entry.bind("<Button-1>", entry_clear)
cnae_entry.bind("<Button-1>", entry_clear)
dni_entry.bind("<Button-1>", entry_clear)


root.mainloop()