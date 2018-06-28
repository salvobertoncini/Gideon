#General import
import random
#import math

#Personal import
import tools
import constraints


def crossover(Population, Pcros):
	Npop = len(Population)
	Num_Op = Npop * Pcros
	Cros_Desc = []

	#print "*** CROSSOVER ***"

	for n in range(0, Num_Op):
		#print "* crossover n. "+str(n)+"*"

		X = []
		Y = []

		"""
		Parent1 = random.SystemRandom().choice(Population)

		Parent2 = random.SystemRandom().choice(Population)
		while Parent1 == Parent2:
			Parent2 = random.SystemRandom().choice(Population)
		"""
		Parent1, Parent2 = random.SystemRandom().sample(Population, 2)

		#normalization Chromosomes length
		max_x = max(len(Parent1[0]), len(Parent2[0]))
		max_y = max(len(Parent1[1]), len(Parent2[1]))

		while max_x > len(Parent1[0]):
			Parent1[0].append(0)
		while max_x > len(Parent2[0]):
			Parent2[0].append(0)
		while max_y > len(Parent1[1]):
			Parent1[1].append(0)
		while max_y > len(Parent2[1]):
			Parent2[1].append(0)

		#break points X, Y
		min_x = min(len(Parent1[0]), len(Parent2[0]))
		min_y = min(len(Parent1[1]), len(Parent2[1]))
		Point_Cross_X = random.randint(1, min_x)
		Point_Cross_Y = random.randint(1, min_y)

		X11 = Parent1[:Point_Cross_X]
		X21 = Parent2[:Point_Cross_X]
		X12 = Parent1[Point_Cross_X:]
		X22 = Parent2[Point_Cross_X:]

		Y11 = Parent1[:Point_Cross_Y]
		Y21 = Parent2[:Point_Cross_Y]
		Y12 = Parent1[Point_Cross_Y:]
		Y22 = Parent2[Point_Cross_Y:]

		X.append(X11 + X22)
		X.append(X11 + X22)
		X.append(X12 + X21)
		X.append(X12 + X21)

		Y.append(Y11 + Y22)
		Y.append(Y12 + Y21)
		Y.append(Y11 + Y22)
		Y.append(Y12 + Y21)

		for i in range(0, 4):
			if [X[i], Y[i]] not in Population and [X[i], Y[i]] not in Cros_Desc:
				Cros_Desc.extend([X[i], Y[i]])

	return Cros_Desc


def mutate_gene(Gene, i):
	pre = Gene[:i]
	post = Gene[i:]
	a = '1' if Gene[i] == 0 else '0'

	return int(pre+a+post, 2)


def mutation(Population, Pmut):
	Npop = len(Population)
	Num_Op = Npop*Pmut
	Mut_Indiv = []

	#print "*** MUTATION ***"

	for n in range(0, Num_Op):
		Individual = random.SystemRandom().choice(Population)

		for i in range(0, len(Individual[0])):
			if random.randint(0, 100) < Pmut:
				Individual[0][i] = mutate_gene('{0:b}'.format(Individual[0][i]), random.SystemRandom().choice(range(len('{0:b}'.format(Individual[0][i])))))

		for i in range(0, len(Individual[1])):
			if random.randint(0, 100) < Pmut:
				Individual[1][i] = mutate_gene('{0:b}'.format(Individual[1][i]), random.SystemRandom().choice(range(len('{0:b}'.format(Individual[1][i])))))

	if Individual not in Population and Individual not in Mut_Indiv:
		Mut_Indiv.append(Individual)

	return Mut_Indiv


def Sreal_function(Individual, i, j):
	summa = 0

	k_iter = len(Individual[0])
	for k in range (0, k_iter):
		x = bool(Individual[0][k][i])
		y = bool(Individual[1][k][j])

		summa = summa | x & y

	return summa, k_iter


def Gaccs_and_Gconf(Sreq, Individual, h, w):
	Gconf = 0
	Gaccs = 0
	k_iter = 0
	DUPA = 0
	for i in range(0, h):
		for j in range(0, w):
			Sreal, k_iter = Sreal_function(Individual, i, j)
			Gconf = Gconf | max(0, (Sreq[i][j] ^ Sreal))
			Gaccs = Gaccs | max(0, (Sreal ^ Sreq[i][j]))

	return Gaccs, Gconf, k_iter


def fitness_function_basic(w1, w2, h, w, Sreq, Individual):
	Gaccs, Gconf, k = Gaccs_and_Gconf(Sreq, Individual, h, w)

	k_constraint = 8

	#maximum number of roles to which an individual user can belong(e.g. 30)
	#constraint_result = constraints.cardinality_constraint_of_role(Individual, k_constraint)

	#maximum number of roles to which a permission can belong(e.g. 30)
	constraint_result = constraints.cardinality_constraint_of_permission(Individual, k_constraint)

	#maximum number of users to which a role can have (e.g. 30, x as the role of CEO)
	#constraint_result = constraints.cardinality_constraint_of_user(Individual, 2, k_constraint)

	#maximum number of permissions to which a role can have (e.g. 30, x as the role of CEO)
	#constraint_result = constraints.cardinality_constraint_of_permission_role(Individual, 2, k_constraint)

	#one individual cannot be a member of both mutually exclusion roles (e.g. 7, 10)
	#constraint_result = constraints.mutually_exclusive_roles(Individual, 2, 3)

	#one individual cannot be a member of both mutually exclusion roles (e.g. 7, 10)
	#constraint_result = constraints.mutually_exclusive_permissions(Individual, 2, 3)

	#mixed result between two constraints: cardinality constraint of permissions and mutually exclusive permissions
	#constraint_result = constraints.cardinality_constraint_of_permission(Individual, k_constraint)
	# + constraints.mutually_exclusive_permissions(Individual, 2, 3)

	#without constraints, pure GA
	#result = pow(w1*k + w2*Gconf + w2*Gaccs, -1)

	result = pow(w1*k + w2*Gconf + w2*Gaccs + w2*constraint_result, -1)

	return result


def fitness_function(Sreq, h, w, Population, w1, w2):
	Population = tools.from_lists_to_binary_matrix(Population)
	"""
	Gaccs = 0
	Gconf = 0
	k = 0

	for i in range(0, len(Population)):
		Gaccs, Gconf, k = Gaccs_and_Gconf(Sreq, Population[i], h, w)
		F_basic = float(1 / (w1*k + w2*Gconf + w2*Gaccs))
		if F_basic > 0:
			print F_basic
	"""
	Population.sort(key=lambda x: fitness_function_basic(w1, w2, h, w, Sreq, x))
	
	Population = tools.from_binary_to_int_matrix(Population)
	return Population


def selection(Sreq, h, w, Population, Npop, New_cross, New_mut, w1, w2):
	#print "*** SELECTION ***"
	Population+=New_cross
	Population+=New_mut

	Population = fitness_function(Sreq, h, w, Population, w1, w2)

	return Population[:Npop]


def access_control_schema(Sreq, h, w, Population, Npop, Tmax, Pcros, Pmut, w1, w2):
	for i in range(0, Tmax):
		print "iteration n. "+str(i+1)
		New_cross = crossover(Population, Pcros)
		New_mut = mutation(Population, Pmut)
		Population = selection(Sreq, h, w, Population, Npop, New_cross, New_mut, w1, w2)

	return Population
