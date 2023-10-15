import socket
import time

# Define the list of hex messages to send
hex_messages = ['78781101086348204028031120030001060a00c60d0a',
                '787805130402bc0a0d0a']

# Define the IP address and port to send the messages to
ip_address = 'localhost'
port = 5023

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the specified IP address and port
s.connect((ip_address, port))

# Iterate over the list of hex messages
for message in hex_messages:
    print(message)
    # Convert the hex message to bytes
    byte_message = bytes.fromhex(message)
    # Send the byte message to the socket
    s.sendall(byte_message)
    # Wait for 2 seconds before sending the next message
    time.sleep(10)

# Close the socket connection
time.sleep(120)
s.close()
