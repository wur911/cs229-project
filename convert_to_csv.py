#!/usr/bin/env python2.7

from astropy.io import fits
import math
import sys
import numpy

# Converts all the data from the fits file into a csv format
# 

if len(sys.argv) == 1:
	print 'Error: please provide a filename!'
	exit()
filename = sys.argv[1]
hdulist = fits.open(filename)
values = []

for x in range(0,len(hdulist[1].data)):
	for y in range(0,20):
		values.append(hdulist[1].data[x][y])
	values.append("\n")

print ','.join([str(n) for n in values])
