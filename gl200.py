import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("38.242.251.130", 5004))


data = "+RESP:GTDAT,271102,867162029332640,6979,T22H59,20240426115205,2683$"

s.send(data.encode())


# while True:
#     print(s.recv(1024))

time.sleep(120)
s.close