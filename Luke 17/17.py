from itertools import takewhile
print max([i for i in takewhile(lambda x: x*4 != int("6"+str(x)[:-1]), range(6, 1000006,10))])

