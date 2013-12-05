#!/usr/lib/python3
import logging
import threading
import time
logging.basicConfig(level=logging.DEBUG,
		format='%(asctime)s (%(threadName)-2s) %(message)s',
		)
def consumer(cond):
	"""wait for the condition and use the resource"""
	logging.debug('starting consumer thread')
	t=threading.currentThread()
	with cond:
		cond.wait()
		logging.debug('resource is available for consumer')
def producer(cond):
	"""set up the resource to be used by consumer"""
	logging.debug('starting producer thread')
	with cond:
		logging.debug('making resource available')
		cond.notifyAll()
if __name__=='__main__':
	condition=threading.Condition()
	t1=threading.Thread(target=consumer,name='t1',
			args=(condition,))
	t2=threading.Thread(target=consumer,name='t2',
			args=(condition,))
	p1=threading.Thread(target=producer,name='p1',
			args=(condition,))
	t1.start()
	time.sleep(1)
	t2.start()
	time.sleep(2)
	p1.start()
