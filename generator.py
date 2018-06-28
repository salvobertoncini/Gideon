#General import
import random

#Personal import
import tools


def from_txt_to_matrix(file_name):
	raw_dataset = tools.open_file(file_name)
	array_replace = raw_dataset.split()

	i, h, w, tot, dataset, Matrix = 0, 0, 0, 0, [], []

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			if h < int(array_replace[i]): 
				h = int(array_replace[i])
			if w < int(array_replace[i+1]):
				w = int(array_replace[i+1])

			dataset.append([int(array_replace[i]), int(array_replace[i+1])])

			i+=2

	#Matrix initialization
	for i in range(0, h):
		temp = []
		for j in range(0, w):
			temp.append(0)

		Matrix.append(temp)

	for x in dataset:
		i = x[0] - 1
		j = x[1] - 1
		Matrix[i][j] = 1
		tot+=1

	return Matrix, h, w, len(array_replace), tot*100/(h*w)


def create_non_null_gene(x):
	temp = ""
	for j in range(0, x):
		temp += str(random.randint(0, 1))

	return temp


def create_chromosome(k, x, Chromosome):
	for i in range(0, k):
		temp_int = 0

		while temp_int == 0:
			temp = create_non_null_gene(x)
			temp_int = int(temp, 2)
		
		Chromosome.append(temp_int)

	return Chromosome


def Population_creation(Npop, h, w):
	Population = []

	for i in range(0, Npop):
		X, Y = [], []

		#generate at most h elements (number of columns, aka number of users)
		k = random.randint(1, h)

		X = create_chromosome(k, h, X)
		Y = create_chromosome(k, w, Y)

		Population.append([X, Y])

	return Population