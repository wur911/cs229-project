#!/usr/bin/env python2.7

from astropy.io import fits
import math
import sys
import numpy

# Usage: findDTW.py file1.fit
# File1 is the fits file of the light curve we are currently looking at

# Assumption: s ends in '.fits'
def process(s,x):
	s = s[:-5]
	return 'csv/' + s + "--attribute" + str(x) + '.csv'

if len(sys.argv) == 1:
	print 'Error: please provide a filename!'
	exit()
if len(sys.argv) == 2:
	print 'Error: please provide a classification!'
	exit()
filename = sys.argv[1]
classification = int(sys.argv[2])
hdulist = fits.open(filename)

attributeIndices = [4,6,8,15,17,19,20]
for x in attributeIndices:
	with open(process(filename,x), 'w') as f:
		for y in range(0,len(hdulist[1].data)):
			f.write(str(hdulist[1].data[y][x]) + ',')
		f.write('\n')
		
	

