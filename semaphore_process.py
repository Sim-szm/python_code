#!/usr/bin/env python
import random
import multiprocessing
import time

class activepool(object):
	def __init__(self):
		super(activepool,self).__init__()
		self.mgr=multiprocessing.Manager()
		self.active=self.mgr.list()
		self.lock=multiprocessing.Lock()
	def makeActive(self,name):
		with self.lock:
			self.active.append(name)
	def makeInactive(self,name):
		with self.lock:
			self.active.remove(name)
	def __str__(self):
		with self.lock:
			return str(self.active)
def works(sem,pool):
	name=multiprocessing.current_process().name
	with sem:
		pool.makeActive(name)
		print('now running:%s '% str(pool))
		time.sleep(random.random())
		pool.makeInactive(name)
if __name__=='__main__':
	pool=activepool()
	sem=multiprocessing.Semaphore(3)
	jobs=[multiprocessing.Process(
		target=works,
		name=str(i),
		args=(sem,pool))
		for i in range(10)]
	for j in jobs:
		j.start()
	for j in jobs:
		j.join()
		print('now running: %s '%str(pool))
