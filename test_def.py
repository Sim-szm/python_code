#!/usr/bin/python3
import random 
def get_int(msg):
	while True:
		print("input integer: ")
		try:
			i=int(input(msg))
			
			if i:
				return i
				break
			else:
				continue
		except ValueError as err :
			print(err)
age=get_int("")
print("get int value as :",age)
print("start merge set :")
def merge(va1,va2):
	final=[]
	va1=sorted(va1)
	va2=sorted(va2)
	while va1 and va2:
		if va1[0]<=va2[0]:
			final.append(va1.pop(0))
		else:
			final.append(va2.pop(0))
	return final+va1+va2
x=[2,3,1,6,4,5]
y=[8,10,9,7]
print(merge(x,y))
print("random value:",random.randint(2,90))
print(random.choice(["sim","go","stay","love"]))

