from collections import deque

q = deque(range(1, 1501))

while len(q) > 1:
	e, _ = q.popleft(), q.popleft()
	q.append(e)

print(e)