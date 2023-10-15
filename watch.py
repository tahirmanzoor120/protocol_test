import socket
# import time
# import binascii

data = "[3G*8809002413*015D*UD,060623,203604,V,51.925765,N, 4.4894833,E,10.12,112.2,0.0,7,100,83,302718,0,00000000,7,255,204,8,3170,49308,150,3170,51919,139,3170,55916,138,3170,49309,129,3170,53243,127,3170,53250,121,3190,53450,118,5,oskar,0:5f:67:74:e5:ba,-77,Erasmus,c:8e:29:42:89:aa,-80,oskar,28:ee:52:ca:4:6,-81,Ziggo1928721,68:2:b8:79:66:40,-81,,6:5f:67:74:e5:ba,-81,120.4]"
# data = "[3G*8809002413*000E*LK,332856,0,62]"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5093))

#s.send(binascii.unhexlify('68680f0504035889905831401700df1a00000d0a'))
# s.send("imei:123456789012345,tracker,151030080103,,F,000101.000,A,5443.3834,N,02512.9071,E,0.00,0;")

s.send(data.encode())

# while True:
#     print(s.recv(1024))

# time.sleep(120)
s.close()