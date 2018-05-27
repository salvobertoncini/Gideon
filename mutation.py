def Mutation(Pop, Pmut):
	Npop = len(Pop)
	Num_Op = Npop * Pmut
	Mut_Indiv = []

	ii = 0

	while ii < Num_Op:
		Individual[ii] = Random(Pop)
		Individual0[ii] = Individual[ii]

		jj_max_X = Lenght_X(Individual[ii])
		jj = 0

		while jj < jj_max_X:
			if Random() <= Pmut:
				Individual[ii].Gene_X[jj] = Mutate(Individual[ii].Gene_X[jj])
			jj += 1

		jj_max_Y = Lenght_Y(Individual[ii])
		jj = 0

		while jj < jj_max_Y:
			if Random() <= Pmut:
				Individual[ii].Gene_Y[jj] = Mutate(Individual[ii].Gene_Y[jj])
			jj += 1

		if Unical(Individual[ii], Pop + Mut_Indiv) == True:
			Mut_Indiv += Individual[ii]
		else:
			Individual[ii] = Individual0

		ii += 1
	

