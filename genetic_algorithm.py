import random

import constraints

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
	#population = constraints.cardinality_constraint_of_role(population, 30)

	#maximum number of roles to which a permission can belong (e.g. 95)
	#population = constraints.cardinality_constraint_of_permission(population, 95)

	#maximum number of users to which a role can have (e.g. 30, x as the role of CEO)
	#population, n = constraints.cardinality_constraint_of_user(population, 3, 10)

	#one individual cannot be a member of both mutually exclusion roles (e.g. 7, 10)
	#population = constraints.mutually_exclusive_roles(population, 15, 20)

	#the mutually exclusive permissions cannot be assigned to the same role (e.g. 8, 20)
	population = constraints.mutually_exclusive_permissions(population, 15, 20)

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
