#!bin/usr/python3
import random 
import math
import decimal
def find_value_like_xml(tag,line):
	opener="<"+tag+">"
	closer="</"+tag+">"
	try:
		i=line.index(tag)
		start=i+len(opener)
		j=line.index(closer)
		return line[start:j]
	except ValueError:
		return None
test_value="there is <red> Rose love</red>"
print("red_value:",(find_value_like_xml("red",test_value)).strip())
str="/usr/local/bin/firefox"
if str.lower().endswith("firefox"):
	print(str.rpartition("/"))
else:
	print("check error !")
def format_part():

	format_t="{who} love you as {type}".format(who="someone",type="crush")
	print(format_t)
	print("[· learn with dict_value ·]:")
	d=dict(thing=" man ",name="Shim Eye Meo")
	stock=["guy","szm_stock"]
	print("the {0[thing]} is called {0[name]}".format(d))
	print("the {0[0]} is called {0[1]}".format(stock))
format_part()
print(decimal.Decimal(3.141592653))
