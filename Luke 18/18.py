from collections import Counter


def concat(seq):
	return ''.join(seq)


def bits(num, nbits=5):
	return str(bin(num)).lstrip('0b').zfill(nbits)[-nbits:]


def xor(a: str, b: str):
	return concat('1' if x != y else '0' for x, y in zip(a, b))


def chunks(seq, n):
	for i in range(0, len(seq), n):
		yield seq[i:i + n]


def char_from_bits(bits):
	return chr(int(bits, 2))

if __name__ == '__main__':
	ALPHABET = 'AÁBDÐEÉFGHIÍJKLMNOÓPRSTUÚVXYÝÞÆÖ'
	CIPHERTEXT = '1110010101000001011000000011101110100101010011011010101101100000010001111101000001010010001011101001100100100011010000110101111101010011100010110001100111110010'

	with open('text.txt') as f:
		COUNTER = Counter(c for c in f.read() if c.isalpha())

	key = concat(bits(ALPHABET.index(c), 5) for c, _ in COUNTER.most_common())
	plaintext_bits = xor(CIPHERTEXT, key)
	plaintext = concat(char_from_bits(byte) for byte in chunks(plaintext_bits, 8))

	print(plaintext)