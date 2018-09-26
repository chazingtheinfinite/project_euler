#!/usr/bin/python
""" Names Score
Author: Kevin Dick
Date: 2018-09-26
---
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
What is the total of all the name scores in the file?
"""

name_file = '../data/names-score.txt'
f = open(name_file, 'r')
name_list = [x.replace('"', '') for x in f.readlines()[0].split(',')]
f.close()


def name_score(position, name):
	name_vals = [ord(char) - 96 for char in name.lower()]
	return position * sum(name_vals)

def inelegant():
	# Sort
	sort_list = sorted(name_list)

	# Sum - List positions uses 1-based indexing (0-base in Python)
	total = 0
	for i in range(1, len(sort_list) + 1): total += name_score(i, sort_list[i-1])
	return total

print inelegant()

