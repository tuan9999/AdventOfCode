f = open('vals.txt', 'r')

while True:
	x = f.readline()
	if not x:
		break
	x = int(x)
	g = open('vals.txt', 'r')
	while True:
		n = g.readline()
		if not n:
			break
		n = int(n)
		h = open('vals.txt', 'r')
		while True:
			y = h.readline()
			if not y:
				break
			y = int(y)
			if x + n + y == 2020:
				print("x = ", x)
				print("n = ", n)
				print("y = ", y)
				print("result = ", x * n * y)
				exit()