def open_file(path):
	file = open(''+path, 'r')
	file_to_read = file.read()
	file.close()

	return file_to_read


def from_lists_to_binary_matrix(Population):
	max_e = 0

	New_Population = []
	for i in Population:
		chromo = []
		for c in i:
			gen = []
			for g in c:
				temp = '{0:b}'.format(g)
				gen.append(temp)

				if len(temp) > max_e:
					max_e = len(temp)

			chromo.append(gen)
		New_Population.append(chromo)
	
	Population = []
	for i in New_Population:
		chromo = []
		for c in i:
			gen = []
			for g in c:
				temp = g
				while len(temp) < max_e:
					temp = '0'+temp
				gen.append(temp)
			chromo.append(gen)
		Population.append(chromo)

	return Population
	
	#Population = [ a.insert(0,'0') gen.append(g) for i in New_Population for c in i for g in c for a in range(len(g), max_e)]


def from_binary_to_int_matrix(Population):
	for i in range(0, len(Population)):
		for c in range(0, len(Population[i])):
			for g in range(0, len(Population[i][c])):
				Population[i][c][g] = int(Population[i][c][g], 2)

	#Population = [int(g, 2) for i in Population for c in i for g in c]
					
	return Population