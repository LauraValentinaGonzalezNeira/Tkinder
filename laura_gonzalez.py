from tkinter import *

Ventana = Tk()
Ventana.geometry("350x300")
Ventana.title("Bienvenido a la ventana")
Ventana.config(bg="blue")

etiqueta = Label(
 Ventana, 
 text='\n Para verificar que todo esta funcionando por favor presione el botón\n',
 bg='blue',
 font='Times 15')
etiqueta.pack()

def verificacion():
  ver = '\n Gracias por presionar el botón, todo funciona bien'
  eti = Label(Ventana, 
   text=ver,
   bg='blue',
   font='Times 15').pack()

boton = Button(Ventana, text="Verificación", command=verificacion)
boton.pack()

Ventana.mainloop()
