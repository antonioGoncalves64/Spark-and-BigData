matrix = [
			[0, 0, 0],
			[1, 1, 1],
			[2, 2, 2],
		 ]

flat = [num for row in matrix for num in row]

print("matrix=", flat)