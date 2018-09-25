#!/usr/bin/python
""" Largest Palindrome Product
Author: Kevin Dick
Date: 2018-09-25
---
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
	return str(number) == str(number)[::-1]

def brute_force(n):
	largest = float("-inf")
	for i in range(n):
		for j in range(n):
			product = i * j
			if is_palindrome(product) and product >= largest: largest = product
	return largest


def reduce_half(n):
	""" 
	Can cut down on processing redundant values by starting from the top and working downwards.
	We can eliminate products by ensureing none fall below the current value of the largest palindrome.
	This way we explore only the fornteir of the highest possible products and eliminate many calls.
	"""
	largest = float("-inf")
	i = n - 1 # Start at the top (finds the largest fastest)
        while i >= 100:
		j = n - 1 # Start at the top...
		while j >= i:
			product = i * j
			if product <= largest: break # Since a*b will forgever be smaller	
			if is_palindrome(product): largest = product
			j -= 1
		i -= 1
        return largest

print brute_force(1000)
print reduce_half(1000)
