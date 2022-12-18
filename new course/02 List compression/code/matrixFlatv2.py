matrix = [
			[0, 0, 0],
			[1, 1, 1],
			[2, 2, 2],
		 ]

flat = []
for row in matrix:
	for num in row:
		flat.append(num)

print("matrix=", flat)