#!/bin/bash

# Script to repeatedly call findDTW on each .fits file
# Writes all the 

cat ../headers.csv >> ../examples.csv
for file in *.fits; do
	../findDTW.py $file
	for csv in *4.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
	for csv in *6.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
	for csv in *8.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
	for csv in *15.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
	for csv in *17.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
	for csv in *19.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
	for csv in *20.csv; do
		cd ../FastDTW-1.1.0/src
		java com.FastDtwTest $csv base 10 >> ../../examples.csv
		cd ../../positive_examples
		rm $csv
	done
done
