"""Reformatted from the 20 November 2025 email; original decoding retained.
Requires a known XYZ byte boundary; not validated against hardware.
"""
import serial

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

def decode_axis(byte):
    sign = -1 if (byte & 0x80) else 1
    value = (byte >> 3) & 0x0F
    return sign * value

print("Lecture XYZ decodees...")
while True:
    data = ser.read(3)
    if len(data) == 3:
        x = decode_axis(data[0])
        y = decode_axis(data[1])
        z = decode_axis(data[2])
        print(f"X={x:2d} Y={y:2d} Z={z:2d}")
