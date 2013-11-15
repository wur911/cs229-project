#!/usr/bin/env python3.2

# Arun Debray. 15 Nov 2013

# Goal: if L is the set of lines in file 1 and M the set of lines in file 2,
# write a file containing L \ M.

# Usage: ./line_util.py input.txt to_remove.txt
#	(spits to stdout)

import sys

def main():
	if len(sys.argv) < 3:
		print("Fool, how do you expect to use me if you don't provide enough filenames?", file=sys.stderr)
	with open(sys.argv[1], 'r') as f:
		all_lines = f.readlines()
		with open(sys.argv[2], 'r') as g:
			remove_lines = set(g.readlines())
			out_lines = [lin for lin in all_lines if lin not in remove_lines]
			for lin in out_lines:
				sys.stdout.write(lin)

if __name__ == '__main__':
	main()
