import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 6038))

data = "$2026,M2CD,0.1.12,NR,01,L,866897055062642,89910273317000539819,O,1,01122023,085154,28.647535,N,77.192764,E,0.00,149.03,09,157.40,Vodafone,31,1,0,0,1,11.7,4.5,0.03,XXX.X,24,1386,X,49282,27FA*"

s.send(data.encode())

while True:
    print(s.recv(1024))

time.sleep(120)

s.close()