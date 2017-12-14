from bitarray import bitarray
from PIL import Image

image = Image.open('knowit_03.png')
red, *_ = image.split()
bits = [x & 1 for x in red.tobytes()]

#byte_string, *_ = bitarray(bits, endian='little').tobytes().partition(b'\0')
#result = byte_string.decode('ascii')

print(bitarray(bits, endian='little').tobytes())