#!/usr/bin/env python3
# To use this script, first argument should be a text file with the list of files you want to filter on (each file name on a new line)
# The second argument should be the extension you want to filter on e.g. "jpg"
#
# An example of the command would look like:
# ./filter_file_list.py list.txt jpg
# This filters the files found in list.txt for extension of jpg e.g. file1.jpg

import re
import sys

def filter_files(files, ext):
	# For this exercise, assume the filenames are provided for you in the first parameter, 'files', a list of strings.
	# ext is the extension you are looking to filter on (e.g. .jpg, .gif, etc.)

	filtered_files = []
	# extract f from list of "files"
	filtered_files = [f for f in files if re.findall(r"\S+\.%s" %ext, f)] 

  
	# `filtered_files` will be a list of strings / filenames, e.g. ['pantheon.jpg', 'funny_cat.jpg']
	return filtered_files

if __name__ == "__main__":
	file_input = open(sys.argv[1], "r")
	file_list = file_input.readlines()
	filtered_list = filter_files(file_list,sys.argv[2])
	filtered_clean = []
	for file in filtered_list:
		file = file.rstrip('\n')
		print(file)
		filtered_clean.append(file)
	print(filtered_clean)
