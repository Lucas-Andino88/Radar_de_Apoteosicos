import tkinter as tk
from tkinter import messagebox 
v = tk.Tk()
v.title("Radar de Apoteósicos")
v.geometry("600x250")
oprobio = 1
def apagado():
    oprobio = 0
def encendido():
    while oprobio == 1:
        if oprobio != 1:
            break
        dato = float(off.get)
        pantalla.config(text="Distancia Respecto al sensor: {dato}")
on = tk.Button(v, text="ENCENDER", width=30)
off = tk.Button(v, text="APAGAR", width=30)
pantalla = tk.Label(v, text="Distancia Respecto al sensor: ", height=3, width=30)
on.grid(row=1, column=1)
off.grid(row=1, column=2)
pantalla.grid(row=2, column=1)
v.mainloop()