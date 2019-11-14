import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

serversocket.bind((host, port))
serversocket.listen(5)

while True:
	clientsocket, addr = serversocket.accept()
	print("Got a connection from %s" % str(addr))
	data = clientsocket.recv(1024)
	rev_data = data.decode()[::-1]
	clientsocket.send(rev_data.encode())
clientsocket.close()

