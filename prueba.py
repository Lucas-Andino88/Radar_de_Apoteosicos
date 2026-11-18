import serial
import time
import tkinter as tk

# Cambia 'COM3' por el puerto de tu Arduino
ser = serial.Serial('COM3 (Arduino Mega or Mega 2560', 9600, timeout=1)
time.sleep(2) # Pausa necesaria mientras se reinicia el Arduino

print("Iniciando lectura del sensor...")

try:
    while True:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            
            # Verifica que la línea no esté vacía antes de convertir
            if linea:
                try:
                    distancia = float(linea)
                    print(f"Distancia actual: {distancia:.2f} cm")
                except ValueError:
                    pass # Ignora lecturas incompletas al iniciar
except KeyboardInterrupt:
    print("\nLectura detenida por el usuario.")
finally:
    ser.close()


