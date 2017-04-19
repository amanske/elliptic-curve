import sys

for line in sys.stdin:
	line = line.strip("\n") #remove newline character from last element on line
	data = line.split(" ")
	p = int(data[0])
	a = int(data[1])
	b = int(data[2])
	ec_points = 0; #stores number of affine points
	residues = []

	i = 0
	j = 0
	#calculate quadtratic residues
	while i < p:
		residues.append((i*i) % p)
		i += 1
	while j < p:
		mod_res = int((j**3 + (a * j) + b) % p) # j^3 + aj + b mod p
		for res in residues:
			if res == mod_res: #if the quadratic residue equals mod_res, we have found a point
				ec_points += 1
		j += 1

	#if the discriminant of the function (-4a^3-27b^2) equals 0, the curve is singular
	if (-4*a**3-27*b**2) % p == 0:
		print(1, ec_points)
	#otherwise its smooth
	else:
		print(0, ec_points)
