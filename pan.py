#General import
import random

#Personal import
import evaluator

"""ANNEX
import operator
"""


def open_file(path):
	#writeLog("file opened: "+path)
	file = open(''+path, 'r')
	file_to_read = file.read()
	file.close()

	return file_to_read


def from_txt_to_dataset(file_name, tag_id, tag_value):
	raw_dataset = open_file(file_name)

	array_replace = raw_dataset.split()
	dataset = []
	i=0

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			dataset.append({""+tag_id: int(array_replace[i]), ""+tag_value: array_replace[i+1]})
			
			i+=2

	return dataset


def list_of_tag(dataset, tag):
	list_tag = []

	for x in dataset:
		if x[""+tag] not in list_tag:
			list_tag.append(x[""+tag])

	return list_tag


def Individual_creation(x_list):
	Individual = ""

	#Creation of chromosomes which lenght is the number of users or permissions
	for i in range(0,len(x_list)):
		Individual += str(random.randint(0, 1))

	return Individual


def create_population(dataset, tag_id, tag_value):
	users_list = list_of_tag(dataset, tag_id)
	permissions_list = list_of_tag(dataset, tag_value)

	#mapped_list = create_mapped_list(dataset, tag_id, tag_value)
	#role_list = create_role_list(mapped_list, tag_value)

	#X = X_Matrix(mapped_list, role_list, tag_id, tag_value)
	#Y = Y_Matrix(mapped_list, role_list, tag_id, tag_value)

	X = []
	Y = []
	Population = []

	for i in range(0,Npop):
		X = (Individual_creation(users_list))
		Y = (Individual_creation(permissions_list))
		Population.append([X, Y])

	return Population


def access_control_scheme_design(population, Npop, Tmax, Pcros, Pmut):
	for i in range(0, Tmax):
		print "iteration n. "+str(i+1)
		Cross_desc = crossover(population, Pcros)
		Mut_Indiv = mutation(population, Pmut)
		population = selection(population, Npop, Cross_desc, Mut_Indiv)

	return population


def crossover(population, Pcros):
	Npop = len(population)
	Num_Op = Npop * Pcros
	
	Cross_desc = []

	for i in range(0, Num_Op):
		X = []
		Y = []
		Descendants = []	

		#Select two DIFFERENT element
		Parent1 = random.SystemRandom().choice(population)
		Parent2 = random.SystemRandom().choice(population)

		#Partition Point
		Point_Cross_X = random.randint(1, min(Lenght_Chromosome(Parent1, 1), Lenght_Chromosome(Parent2, 1)))
		Point_Cross_Y = random.randint(1, min(Lenght_Chromosome(Parent1, 2), Lenght_Chromosome(Parent2, 2)))

		#Partition of Parents
		X11 = Left(Parent1[0], Point_Cross_X)
		X12 = Right(Parent1[0], Point_Cross_X)
		X21 = Left(Parent2[0], Point_Cross_X)
		X22 = Right(Parent2[0], Point_Cross_X)

		Y11 = Left(Parent1[1], Point_Cross_Y)
		Y12 = Right(Parent1[1], Point_Cross_Y)
		Y21 = Left(Parent2[1], Point_Cross_Y)
		Y22 = Right(Parent2[1], Point_Cross_Y)

		#formation of Descendants
		X.append(X11 + X22)
		X.append(X12 + X21)
		X.append(X11 + X22)
		X.append(X12 + X21)
		
		Y.append(Y11 + Y22)
		Y.append(Y12 + Y21)
		Y.append(Y11 + Y22)
		Y.append(Y12 + Y21)

		for j in range(0, 4):
			Descendants.append([X[j], Y[j]])
			if Descendants[j] not in population:
				if Descendants[j] not in Cross_desc:
					Cross_desc.append(Descendants[j])

	return Cross_desc


def mutation(population, Pmut):
	Npop = len(population)
	Num_Op = Npop * Pmut
	Pmut2 = 40

	Mut_Indiv = []

	for i in range(0, Num_Op):
		Individual = []

		#Selection of individual which will be mutated
		Individual = random.SystemRandom().choice(population)

		#Mutation chromosome X of Individual
		j_max_X = Lenght_Chromosome(Individual, 1)
		for j in range(0, j_max_X):
			if random.randint(0,100) < Pmut:
				tmp = list(Individual[0])
				tmp = Mutate(tmp, j)
				Individual[0] = ''.join(tmp)

		#Mutation chromosome Y of Individual
		j_max_Y = Lenght_Chromosome(Individual, 2)
		for j in range(0, j_max_Y):
			if random.randint(0,100) < Pmut:
				tmp = list(Individual[1])
				tmp = Mutate(tmp, j)
				Individual[1] = ''.join(tmp)

		if Individual not in population:
			if Individual not in Mut_Indiv:
				Mut_Indiv.append(Individual)

	return Mut_Indiv


def selection(population, Npop, Cross_desc, Mut_Indiv):
	population.extend(Cross_desc)
	population.extend(Mut_Indiv)

	#Deletion of the individuals with the worst values of the fitness function
	population = sort_by_fitness_function(population)
	
	#maximum number of roles to which an individual user can belong(e.g. 30)
	#population = cardinality_constraint_of_role(population, 30)

	#maximum number of roles to which a permission can belong (e.g. 95)
	#population = cardinality_constraint_of_permission(population, 95)

	#maximum number of users to which a role can have (e.g. 30, x as the role of CEO)
	#population, n = cardinality_constraint_of_user(population, 3, 10)

	#one individual cannot be a member of both mutually exclusion roles (e.g. 7, 10)
	#population = mutually_exclusive_roles(population, 15, 20)

	#the mutually exclusive permissions cannot be assigned to the same role (e.g. 8, 20)
	population = mutually_exclusive_permissions(population, 15, 20)

	del population[Npop:]
	
	return population


def Lenght_Chromosome(Individual, x):
	if x == 1:
		#return Chromosome X lenght
		return len(Individual[0])
	else:
		#return Chromosome Y lenght
		return len(Individual[1])


def Left(Chromosome, cross_point):
	return Chromosome[:cross_point]


def Right(Chromosome, cross_point):
	return Chromosome[cross_point:]


def Mutate(chromosome, j):
	if chromosome[j] == '0':
		chromosome[j] = '1'
	else:
		chromosome[j] = '0'

	return chromosome


def sort_by_fitness_function(population):
	#sort by the X ascend
	population.sort(key=lambda tup:tup[0])

	return population


def cardinality_constraint_of_role(population, N):
	population_x = []

	for individual in population:
		#control of chromosome X
		tmp = list(individual[0])
		count = 0
		for x in tmp:
			if x == '1':
				count +=1 

		if count < N:
			individual[0] = ''.join(tmp)
			population_x.append(individual)

	return population_x


def cardinality_constraint_of_permission(population, N):
	population_x = []

	for individual in population:
		#control of chromosome X
		tmp = list(individual[1])
		count = 0
		for x in tmp:
			if x == '1':
				count +=1 

		if count < N:
			individual[1] = ''.join(tmp)
			population_x.append(individual)

	return population_x


def cardinality_constraint_of_user(population, N, i):
	#input: population, max number of user with the role, index of role in the binary chromosome X
	population_x = []
	count = 0

	for individual in population:
		#control of chromosome X
		tmp = list(individual[0])

		if tmp[i] == '1':
			count +=1 

		if count < N:
			individual[0] = ''.join(tmp)
			population_x.append(individual)

	return population_x, count


def mutually_exclusive_roles(population, i, j):
	population_x = []

	for individual in population:
		#control of chromosome X
		tmp = list(individual[0])

		if tmp[i] == '1' and tmp[j] == '1':
			print "found: "+individual[0]+"\n"
		else:
			individual[0] = ''.join(tmp)
			population_x.append(individual)

	return population_x


def mutually_exclusive_permissions(population, i, j):
	population_x = []

	for individual in population:
		#control of chromosome X
		tmp = list(individual[1])

		if tmp[i] == '1' and tmp[j] == '1':
			print "found: "+individual[1]+"\n"
		else:
			individual[1] = ''.join(tmp)
			population_x.append(individual)

	return population_x	


#def anti-association_rule_between_permissions(population)
#def anti-association_rule_between_roles(population)


if __name__ == '__main__':
	dataset_name = 'domino'
	file_name = '../datasets/'+dataset_name+'.txt'

	tag_id = 'user'
	tag_value = 'permission'

	#Number of individuals in population
	Npop = 200
	#Max number of iterations
	Tmax = 10
	#Probability of crossover
	Pcros = 15
	#Probability of mutation
	Pmut = 10

	t0 = evaluator.start_timer()

	dataset = from_txt_to_dataset(file_name, tag_id, tag_value)
	population = create_population(dataset, tag_id, tag_value)
	config = access_control_scheme_design(population, Npop, Tmax, Pcros, Pmut)

	evaluator.end_timer(t0)

	#print config
