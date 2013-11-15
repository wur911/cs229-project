from astropy.io import fits
import math
import sys
import numpy
filename = raw_input("Enter a fits file\n")
hdulist = fits.open(filename)

feature_list = []

# find the mean
print "Find the arithmetic mean"
for x in range(0,20):
	sumvalues = 0
	for y in range(0,len(hdulist[1].data)):
		if not math.isnan(hdulist[1].data[y][x]):
			sumvalues += hdulist[1].data[y][x]
	avg = sumvalues/len(hdulist[1].data)
	print avg
	feature_list.append(avg)
	
# find the max and min
print "Find the max"
for x in range(0,20):
	maxval = -sys.maxint-1
	for y in range(0,len(hdulist[1].data)):
		if not math.isnan(hdulist[1].data[y][x]):
			if hdulist[1].data[y][x] > maxval:
				maxval = hdulist[1].data[y][x]
	print maxval
	feature_list.append(maxval)
print "Find the min"
for x in range(0,20):
	minval = sys.maxint
	for y in range(0,len(hdulist[1].data)):
		if not math.isnan(hdulist[1].data[y][x]):
			if hdulist[1].data[y][x] < minval:
				minval = hdulist[1].data[y][x]
	print minval
	feature_list.append(minval)
	
# find the range
print "Find the range"
for x in range(0,20):
	feature_list.append(feature_list[20+x] - feature_list[40+x])

# find the standard deviation

