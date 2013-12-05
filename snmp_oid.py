#!/usr/bin/env python

import os,sys
import string
import re
import urllib2


if __name__ == '__main__':

	if len(sys.argv) != 2:
		sys.stderr.write("Please provide one OID number or string to lookup.\n");
		sys.exit(1)

	flag = 0
	found = False

	r = re.compile('^[0-9\\.]+$')
	if r.match(sys.argv[1]):
		r = re.compile('^1\\.3')
		if r.match(sys.argv[1]):
			flag = 1
		else:
			sys.stderr.write("Please provide the full OID number under .iso.org!\n")
			sys.exit(1)
	
	try:
		req = urllib2.Request('http://www.kix.in/plan9/mirror/sources/contrib/gabidiaz/root/lib/ndb/snmp')
		resp = urllib2.urlopen(req)
		oid = resp.readline()
		name = resp.readline()
		while oid and name:
			if flag == 1:
				if oid.find(sys.argv[1]) != -1:
					print name
					found = True
					break
			else:
				n = name.lower().find(sys.argv[1].lower())
				if n != -1:
					print oid
					found = True
					if n+len(sys.argv[1]) < len(name)-1:
						print name
			oid = resp.readline()
			name = resp.readline()
		if not found:
			print "Not found!"
		sys.exit(0)
	except IOError:
		sys.stderr.write("Probably you don't have Internet.\n")
		sys.exit(1)

