import socket
import time

# Define the hex message to send
hex_message = '7e02000041013655298851138a000000800000000b02ee173b07517693004e0000006623061114203930011f31010ee10200215d0b01012ed08a48061d2307c00402010157080000000000000000bf7e'

# Define the IP address and port to send the messages to
ip_address = 'localhost'
port = 5015

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the specified IP address and port
s.connect((ip_address, port))

# Convert the hex message to bytes
byte_message = bytes.fromhex(hex_message)

# Send the byte message to the socket
s.sendall(byte_message)

# Close the socket connection
time.sleep(60)
s.close()
