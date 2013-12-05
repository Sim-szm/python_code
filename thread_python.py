#!/bin/usr/python 
import time
import threading
def test(num):
	cnt=0
	while cnt<10:
		print (' thread %d echo this : %d' %(num,cnt))
		time.sleep(1)
		cnt+=1
threads=[]
def worker():
	for i in range(2):
		t=threading.Thread(target=test,args=(i,))
		threads.append(t)
		t.start()
if __name__=='__main__':
	worker()
