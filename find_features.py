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
print ",".join([str(n) for n in featurelist])

# find the max and min
#print "Find the max"
#for x in range(0,20):
#	filt_vals = [m[x] for m in hdulist[1].data if not math.isnan(m[x])]
#	maxval = max([m[x] for m in hdulist[1].data if not math.isnan(m[x])])
#	feature_list.append(max(filt_vals) if len(filt_vals) != 0 else 0) # I don't know how else to signal it
#
#	maxval = -sys.maxint-1
#	for y in range(0,len(hdulist[1].data)):
#		if not math.isnan(hdulist[1].data[y][x]):
#			if hdulist[1].data[y][x] > maxval:
#				maxval = hdulist[1].data[y][x]
#	print maxval
#	feature_list.append(maxval)
#print "Find the min"
#for x in range(0,20):
#	minval = sys.maxint
#	for y in range(0,len(hdulist[1].data)):
#		if not math.isnan(hdulist[1].data[y][x]):
#			if hdulist[1].data[y][x] < minval:
#				minval = hdulist[1].data[y][x]
#	print minval
#	feature_list.append(minval)
	
# find the range
#print "Find the range"
#for x in range(0,20):
#	feature_list.append(feature_list[20+x] - feature_list[40+x])

# find the standard deviation
#print "Find the standard deviation"
#for x in range(0,20):
#	sumsquares = 0
#	for y in range(0,len(hdulist[1].data)):
#		if not math.isnan(hdulist[1].data[y][x]):
#			sumsquares += (hdulist[1].data[y][x]-feature_list[x])**2
#	variance = sumsquares/len(hdulist[1].data)
#	stdev = variance**0.5
#	feature_list.append(stdev)

#print ' '.join([str(n) for n in feature_list])
