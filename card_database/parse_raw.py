import sys
import os

skip_counter = 1
dbfile = open(sys.argv[1],"r")
parsed_lines = []
for line in dbfile:
	if skip_counter % 2 == 0:
		parsed_lines.append(line)
	skip_counter += 1
dbfile.close()
os.remove(sys.argv[1] + ".parsed")
dbfile = open(sys.argv[1] + ".parsed","a")
for line in parsed_lines:
	dbfile.write(line)