from tkinter import * 

root = Tk()
root.title('Covidayudas/Empresa')
root.geometry('323x400')

my_canvas = Canvas(root, width=323, height=400)
my_canvas.pack(fill="both", expand=True)

#Boxes

nombre_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
cif_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
cnae_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
ingreso_entry = Entry(root, font=("helvetica", 16), width=14, fg="#336d92", bd=0)
nombre_entry.insert(0, "Nombre")
cif_entry.insert(0, "CIF")
cnae_entry.insert(0, "CNAE")
ingreso_entry.insert(0, "Ingreso Anual")


#ad boxes to canvas
nombre_window = my_canvas.create_window(34, 50, anchor="nw", window=nombre_entry)
cif_window = my_canvas.create_window(34, 100, anchor="nw", window=cif_entry)
cnae_window = my_canvas.create_window(34, 150, anchor="nw", window=cnae_entry)
ingreso_window = my_canvas.create_window(34, 200, anchor="nw", window=ingreso_entry)


#button
send_btn = Button(root, text= "Send", font=("Helvetica", 20 ), width=15, fg="#336d92")
send_btn_window = my_canvas.create_window(34, 300, anchor="nw", window=send_btn)


def entry_clear(e): 
    
    if nombre_entry.get() == 'Nombre' or cif_entry.get() == 'CIF' or cnae_entry.get() == 'CNAE' or ingreso_entry.get() == 'Ingreso Anual' : 
        nombre_entry.delete(0, END)
        cif_entry.delete(0, END)
        cnae_entry.delete(0, END)
        ingreso_entry.delete(0, END)



nombre_entry.bind("<Button-1>", entry_clear)
cif_entry.bind("<Button-1>", entry_clear)
cnae_entry.bind("<Button-1>", entry_clear)
ingreso_entry.bind("<Button-1>", entry_clear)



root.mainloop()