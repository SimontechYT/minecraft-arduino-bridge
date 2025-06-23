import serial
import time
from pynput import mouse

# Cambia 'COM3' con la porta seriale del tuo Arduino
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Attendi apertura porta

def on_click(x, y, button, pressed):
    if button == mouse.Button.right and pressed:
        print(f"Click destro rilevato a ({x}, {y}) - accendo LED")
        arduino.write(b'r')

try:
    print("Ascolto click destro del mouse... premi Ctrl+C per uscire")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\nChiusura programma")
finally:
    arduino.close()
