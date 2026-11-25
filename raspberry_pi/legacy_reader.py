import serial
import time

# ---- CONFIGURATION ----
PORT = "COM8"  # Remplace par le port série de ta carte
BAUDRATE = 115200
TIMEOUT = 1    # en secondes

# Ouvre le port série
ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)

def read_accel():
    while True:
        # Lit un octet
        byte = ser.read(1)
        if len(byte) == 0:
            continue  # rien reçu, on attend

        byte_val = byte[0]

        # Les 2 bits de l'ID
        axis_id = (byte_val & 0b11000000) >> 6
        # Les 6 bits de données
        data = byte_val & 0b00111111

        # Identifier l'axe
        if axis_id == 0b11:
            axis = 'X'
        elif axis_id == 0b10:
            axis = 'Y'
        elif axis_id == 0b01:
            axis = 'Z'
        else:
            axis = 'Unknown'

        print(f"Axe: {axis}, Data: {data}")

try:
    print("Lecture des données accéléromètre...")
    read_accel()
except KeyboardInterrupt:
    print("Fermeture du port série")
    ser.close()
