#!/usr/bin/env python3
la=[1,2,3,4]
lb=[4,5,6,7]
for (x,y) in  zip(la,lb):
	print(x,y,' -- ',x+y)
d1=['spam','stak','sbak']
d2=[1,2,3]
d3=dict(zip(d1,d2))
for key in d3.keys():
	print(key,d3[key])

