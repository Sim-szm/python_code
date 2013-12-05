#!/usr/bin/python3
x="sim"
if len(x)<3:
	print(x);
elif len(x)>=3:
	print("Right:",x,"start my work ：");
else:
	print("notthing doing here !");
y=["love","is","not","a","good","thing"]

for x in y:
		print(x);
for j in x:
	print("second loop :",j);
print("start input—check integer：")
s=input("enter an integer ")
try :
	i=int(s)
	print("valid integer entered :",i)
except ValueError as err:
	print(err)
print(5+6)
print("test + string :")
va="sim"
va+="wait"
print(va);
