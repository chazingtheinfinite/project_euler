#!/usr/bin/python
""" Large Sum
Author: Kevin Dick
Date: 2018-09-25
---
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

num_file = './data/large-sum.txt'
nums = []
f = open(num_file, 'r')
for line in f: nums.append(line.strip())
f.close()

def brute_force():
	total = 0
	for num in nums: total += int(num)
	return int(str(total)[:10])

def string_traversal():
	""" TODO
	"""
	return ""

print brute_force()
print string_traversal()
