import serial


with serial.Serial("/dev/ttyACM0", 9600, timeout=0.5) as serial_port:
    serial_port.write(b'S14324')
