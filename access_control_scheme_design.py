"""
Input: 
	Number of individuals in population (Npop), 
	maximal number of iterations (Tmax), 
	set of criteria (Criteria), 
	probability of crossover (Pcros), 
	probability of mutation (Pmut).
Output: 
	Access control scheme (Config2), where to the maximal degree all the criteria are satisfied
"""

# personal import
import crossover
import mutation
import selection


def access_control_scheme_design(Npop, Tmax, Criteria, Pcros, Pmut):
	Pop = []
	i = 0
	Tcurr = 0

	while i < Npop:
		Ind_i = random(Config)
		Pop.append(Ind_i)
		i+=1

	while Tcurr < Tmax:
		Crossover(Pop, Pcros)
		Mutation(Pop, Pmut)
		Selection(Pop, Criteria)
		Config2 = max_index()
		Tcurr += 1

	return Config
