#!/bin/bash

# Repeatedly run the feature vector generator on all of the files, and spit to stdout.
# This is not a super insightful script, but it ought to be useful.

# The idea is that you can redirect this into a file and have one feature vector per line.

for file in *.fits; do
	../find_features.py $file
done
