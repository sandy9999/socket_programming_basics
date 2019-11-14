import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 10000
serversocket.bind((host, port))

data, addr = serversocket.recvfrom(1024)
if data:
	print("Received " + data.decode())
	rev_data = data.decode()[::-1]
	print("Sending " + rev_data)
	serversocket.sendto(rev_data.encode(), addr)
serversocket.close()
