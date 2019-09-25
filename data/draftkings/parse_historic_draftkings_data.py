import csv
import glob
import os
import re

filenames = glob.glob('./raw/*.html')
outfile = 'draftkings_data.csv'
all_lines = []

for fn in filenames:
	current_lines = []
	with open(fn, 'r') as f:
		lines = f.readlines()
	for l in lines:
		if type(re.search(r"\d+;\d+;\d+;.*;.*;.*;.*;.*;.*;\d+", l)) == type(None):
			pass
		else:
			all_lines.append(l.replace(',', '').replace(';', ','))

with open(outfile, 'w', newline='') as f:
	for l in all_lines:
		f.write(l)
