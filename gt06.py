import socket
import time

# Define the list of hex messages to send
hex_messages = ['78781101086110006483190820030001060a00c60d0a',
                # '78780a13047d0400020003b1e40d0a',
                # '78780a13049405000200031dc00d0a',
                '78781f1218040410342bc805479e400d308580003c85012edc2b0573b34700068d630d0a']

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
    response = s.recv(1024)
    hex_data = ''.join([format(byte, '02x') for byte in response])
    # Print the response
    print("Response from server:", hex_data)
    # Wait for 2 seconds before sending the next message
    time.sleep(10)

# Close the socket connection
time.sleep(120)
s.close()
