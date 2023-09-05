#Crear un conversor de unidades
def millas_a_kilometros():
    kilometros = MILLAS.get() * 1.60934
    message = str(MILLAS.get()) + " Millas equivalen a " + str(kilometros) + " kilometros. "
    messagebox.showinfo(message=message)


def centimetros_a_metros():
    metros = CENTIMETROS.get() / 100
    Message =str(CENTIMETROS.get()) + " Centimetros equivalen a" + str(metros) + " Metros. "
    messagebox.showinfo(message=Message)


    
def milimetros_a_centimetros():
    centimetros = MILIMETROS.get() / 10
    message = str(MILIMETROS.get()) + " Milimetros equivalen a " + str(centimetros) + " Centimetros. "
    messagebox.showinfo(message= message)





def conversor():
    global MILLAS, CENTIMETROS, MILIMETROS
    if opcion.get() == 1:
        lblmillas = Label(text="Ingrese la cantidad de millas que desea convertir: ").place(x=200, y=50)
        MILLAS = IntVar()
        txtMillas = Entry(textvariable=MILLAS).place(x=450, y=30)

        btnConvertio = Button(text="Convertir", command=millas_a_kilometros).place(x=330, y=75)

    elif opcion.get() == 2:
         lblcentimetros = Label(text="Ingrese la cantidad de centimetros que desea convertir: ").place(x=200, y=50)
         CENTIMETROS = IntVar()
         txtCentimetros = Entry(textvariable=CENTIMETROS).place(x=450, y=30)
    
         btnConvertio = Button(text="Convertir", command=centimetros_a_metros).place(x=330, y=75)

    elif opcion.get() == 3:
        lblmilimetros = Label(text="Ingrese la cantidad de milimetros que desea convertir: ").place(x=200, y=50)
        MILIMETROS = IntVar()
        txtMilimetros = Entry(textvariable=MILIMETROS).place(x=450, y=30)
    
        btnConvertio = Button(text="Convertir", command=milimetros_a_centimetros).place(x=330, y=75)


from tkinter import *
from tkinter import messagebox


Interfaz = Tk()

Interfaz.geometry("600x110+650+400")
Interfaz.title("Conversor")

LblOpcion = Label(text="Seleccione la opcion que desea: ").place(x=10, y=10)
opcion = IntVar()
rdB1 = Radiobutton(text="MILLAS A KILOMETROS", value=1, variable=opcion, command=conversor).place(x=10, y=30)
rdB2 = Radiobutton(text="CENTIMETROS A METROS", value=2, variable=opcion, command=conversor).place(x=10, y=50)
rdB3 = Radiobutton(text="MILIMETROS A CENTIMETROS", value=3, variable=opcion, command=conversor).place(x=10, y=70)

Interfaz.mainloop()

