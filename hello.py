#!/usr/bin/env python3
import sys,os
print("hello","Python","world");
print(sys.platform,os.getcwd(),"\nstart threading :\n")
#exec(open('thread_python.py').read())
while True:
	recv=input("enter data: ")
	if recv == 'stop':
		break
	elif recv.isdigit()==True :
		print("value is ".upper(),int(recv)*2)
	else:
		print('Bad '.upper()*4)
print("Bye")
