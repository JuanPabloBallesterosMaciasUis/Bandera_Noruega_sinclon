#Se importa libreria tkinter con todas sus funciones

from tkinter import *

# Ejercicio 1 tkinter 

#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas UIS")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("725x500")



# Color de la ventana
ventana_principal.config(bg="black")

#--------------------
#frame entrada datos
#--------------------



frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg = "red", width = 710 , height = 480)
frame_rojo.place(x = 10, y = 10)


frame_blanco_1 = Frame(ventana_principal)
frame_blanco_1.config(bg = "white", width = 710 , height = 120)
frame_blanco_1.place(x = 10, y = 198)


frame_blaco_2 = Frame(ventana_principal)
frame_blaco_2.config(bg = "white", width = 120 , height = 480)
frame_blaco_2.place(x = 225, y = 10)

frame_azul_1 = Frame(ventana_principal)
frame_azul_1.config(bg = "navy", width = 710 , height = 60)
frame_azul_1.place(x = 10, y = 228)

frame_azul_2 = Frame(ventana_principal)
frame_azul_2.config(bg = "navy", width = 60 , height = 480)
frame_azul_2.place(x = 255, y = 10)


ventana_principal.mainloop()