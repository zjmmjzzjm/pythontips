import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.arin.net", 43))

#convert string to bytes, socket need bytes, argv[1] is an ip address
s.send((sys.argv[1] + "\r\n").encode())

#declares a bytes
response = b""
while True:
    data = s.recv(4096)
    response += data
    if not data:
        break
s.close()

#convert bytes to string
print(response.decode())
