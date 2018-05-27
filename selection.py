def Selection(Pop, Npop):
	Pop = Pop + Cross_Desc + Mut_Indiv

	ii_max = len(Pop)

	Pop = Sort(Pop, F)

	ii = Npop

	while ii < ii_max:
		Deleting(Pop, Individual[ii])
		ii += 1

