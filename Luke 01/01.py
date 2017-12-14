import re


def n_gram(str, n):
	return "".join(sorted("".join([str[i:i+n] for i, _ in enumerate(str) if len(str[i:i+n]) == n])))
	
	
def n_gram_range(word_to_match, word_to_try):
	gram, correct_word = -1, None
	for i in range(1, len(word_to_try)):
		word = n_gram(word_to_try, i)
		if word == word_to_match:
			gram, correct_word = i, word_to_try
			break
	return gram, correct_word	
	

word_to_decipher = "".join(sorted("aeteesasrsssstaesersrrsse"))

with open("wordlist.txt", "rU") as file:
	for line in file:
		if re.match(r"^[serat]+$", line):
			gram, word = n_gram_range(word_to_decipher, line.strip())
			if gram != -1:
				print "%d-%s" % (gram, word)