#!/usr/bin/env python2.7

from astropy.io import fits
import math
import sys
import numpy

# Modified this to accept a filename on the command line.
# This will be easier to weave into larger scripts.
#filename = raw_input("Enter a fits file\n")

# Usage: ./findfeatures.py filename
if len(sys.argv) == 1:
	print 'Error: please provide a filename!'
	exit()
filename = sys.argv[1]
hdulist = fits.open(filename)

featurelist = []
attributeIndices = [3,5,7,14,16,18,19]

# find the mean
for x in attributeIndices:
	sumvalues = 0
	for y in range(0,len(hdulist[1].data)):
		if not math.isnan(hdulist[1].data[y][x]):
			sumvalues += hdulist[1].data[y][x]
	avg = sumvalues/len(hdulist[1].data)
	featurelist.append(avg)

# find the max and min
for x in range(0,20):
	filt_vals = [m[x] for m in hdulist[1].data if not math.isnan(m[x]) and m[x]!=0]
	maxval = max(filt_vals)
	minval = min(filt_vals)
	feature_list.append(maxval if len(filt_vals) != 0 else 0)
	feature_lit.append(minval if len(filt_Vals) != 0 else 0)

print ",".join([str(n) for n in featurelist])
