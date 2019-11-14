import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 10000

strg = input("Enter a string you want to send for reversing")
s.sendto(strg.encode(), (host, port))
data, server = s.recvfrom(1024)
print(data.decode())
s.close()
