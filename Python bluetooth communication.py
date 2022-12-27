import bluetooth

# Create a Bluetooth socket
bd_addr = "00:11:22:33:44:55" # Replace with the MAC address of your HC-05 module
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))

# Send a message over the Bluetooth connection
message = "Hello, World!"
sock.send(message)

# Close the socket when finished
sock.close()
