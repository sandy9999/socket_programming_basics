import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

s.connect((host, port))


strg = input("Enter a string to send to sender for reversing")
s.send(strg.encode())
rev_strg = s.recv(1024)
print(rev_strg.decode())
s.close()

