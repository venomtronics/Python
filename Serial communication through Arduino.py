import serial

# Open a serial connection to the Arduino
ser = serial.Serial("COM3", 9600)

# Send a message to the Arduino
message = "Hello, Arduino!"
ser.write(message.encode())

# Read a response from the Arduino
response = ser.readline().decode().strip()
print(response)

# Close the serial connection
ser.close()
