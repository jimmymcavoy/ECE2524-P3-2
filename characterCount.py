#! /usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser(description='File and search input')

parser.add_argument("--f")

parser.add_argument("--s")

args = parser.parse_args()

f = args.f

s = args.s

print(f)

print(s)
