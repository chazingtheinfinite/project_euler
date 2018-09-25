#!/usr/bin/python
""" Letter Number Counts
Author: Kevin Dick
Date: 2018-09-25
---
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

def brute_force():
	"""
	Requires the num2words package.
	"""
	from num2words import num2words
	total = 0
	for i in range(1,1001):
		word = num2words(i).replace(' ', '').replace('-', '')
		total += len(word)
	return total

print brute_force()
