import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("43.205.159.137", 17010))

data = "$LGN,XY45DX3423,861100064831908,1.ONTC,020.229685,N,078.898735,E,C27326CF*"
# data = "$NRM,WTEX,1.ONTC,NR,01,L,861100064831908,XY45DX3423,1,29042024,170000,28.6084,N,77.2931,E,0.1,000.00,31,0337.29,0.00,0.40,CellOne,0,1,027.0,004.1,0,C,15,404,66,0950,958e,c3e4,256d,11,94b1,094f,11,96a4,256d,11,94cc,094f,09,0000,00,200.000,200.000,008609,1955.604,-,1.0,0,0,23_08_23_1_49._W_1_1_1_95,516A2C42*"

s.send(data.encode())

print("Packet sent.")
response = s.recv(1024)
hex_data = ''.join([format(byte, '02x') for byte in response])
print("Response from server:", hex_data)

time.sleep(10)

s.close()