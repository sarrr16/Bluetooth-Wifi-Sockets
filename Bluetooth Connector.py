import socket

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

s.connect(("D8:C0:A6:BB:F8:FC", 1))

s.send(b"Hello")

data = s.recv(1024)
print(data)

s.close()