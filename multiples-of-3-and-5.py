#!/usr/bin/python
""" Multiple of 3 and 5
Author: Kevin Dick
Date: 2018-09-24
---
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def brute_force(n):
	sum = 0
	for i in range(n):
		if i % 3 == 0 or i % 5 == 0: sum += i
	return sum

def count_multiples(n):
	"""
	Every three numbers is a multiple of 3.
	Every five numbers is a multiple of 5.
	Thus, 3 times the triangular number of floor(1000 / 3)  and 
	5 * triangular number of floor(1000 / 5)
	==> 3 * (333 * 334 / 2) + 5 * (199 * 200 / 2)
	"""
	threes = (n // 3) - 1      # Should be 333
	fives = (n // 5) - 1 # Should be 199
	return 3 * (threes * (threes + 1) / 2) + 5 * (fives * (fives + 1) / 2)

print brute_force(1000)
print count_multiples(1000)
