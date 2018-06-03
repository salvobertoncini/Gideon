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
			#print "found: "+individual[0]+"\n"
			pass
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
			#print "found: "+individual[1]+"\n"
			pass
		else:
			individual[1] = ''.join(tmp)
			population_x.append(individual)

	return population_x	


#def anti-association_rule_between_permissions(population)
#def anti-association_rule_between_roles(population)