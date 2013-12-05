#!/usr/bin/env python
import _socket
import threading
print (_socket.gethostname()," ")
def func():
	sock=_socket.socket(_socket.AF_INET,_socket.SOCK_STREAM)
	server_address=('localhost',9527)
	sock.connect(server_address)
	while True:
		message="select * from weathers where city_name='西安'"
		sock.sendall(message.encode())
		data=sock.recv(2048)
		if not data : 
			break
		else :
			print (data.decode())
	sock.close()
if __name__=='__main__':
	jobs=[]
	for i in range(5):
		t=threading.Thread(target=func)
		jobs.append(t)
		t.start()

