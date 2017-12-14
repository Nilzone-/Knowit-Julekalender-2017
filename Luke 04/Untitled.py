from itertools import permutations, takewhile
from collections import Counter
word = "civic"

def is_palindrome(word):
	return word == word[::-1]

def break_down(word):
	odd,even = 0, 0
	for k, v in Counter(word).most_common():
		odd = odd+1 if v & 1 else odd
	return len(word), odd, even
	
from collections import Counter

word_length, odd, even = break_down(word)

print "word_length: %d" % word_length
print "odds: %d" % odd
print "evens: %d" % even

if not word_length & 1 and odd > 1:
	print "\nno palindrome"
elif word_length & 1 and even > 1:
	print "\npalindrome"
