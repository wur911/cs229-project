# from liblinearutil import *
from astropy.io import fits
import math
filename = raw_input("Enter a fits file\n")
hdulist = fits.open(filename)
# find the mean
for x in range(0,20):
	sumvalues = 0
	for y in range(0,len(hdulist[1].data)):
		if not math.isnan(hdulist[1].data[y][x]):
			sumvalues += hdulist[1].data[y][x]
	avg = sumvalues/len(hdulist[1].data)
	print avg
# find the max and min
for x in range(0,20):

# find the range

# find the standard deviation
