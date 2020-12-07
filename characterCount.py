#! /usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description='File and search input')

parser.add_argument("--filename", required = True, type = str, help = "File you would like to search")

parser.add_argument("--search", required = True, help = "Character or string you would like to search for")

args = parser.parse_args()

fileName = args.filename

searchTerm = args.search

print("Searching for " + "\'" + searchTerm + "\'" + " within " + fileName + 
" ...")

file = open(fileName, 'r').read()

count = file.count(searchTerm)

if count != 0:
	print("Found " + str(count) + " times in file!")
else:
	print("Not found in file!")
		
		
		
		

