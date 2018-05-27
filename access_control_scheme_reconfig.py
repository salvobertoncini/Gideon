"""
Input: 
	Number of individuals in population (Npop), 
	maximal number of iterations (Tmax), 
	set of criteria (Criteria), 
	probability of crossover (Pcros), 
	probability of mutation (Pmut), 
	current scheme (Config_Cur), 
	set of criteria (Criteria), 
	new required values of criteria (Values_New).
Output: 
	New access control scheme (Config_New)
	Criteria(Config_New) = Values_New, 
	min(Config_New - Config_Cur).
"""

# personal import
import crossover
import mutation
import selection


def access_control_scheme_reconfig(Npop, Tmax, Criteria, Pcros, Pmut, Config_cur, Values_New):
	GeneratingInitialPopulation(Npop)
	Tcurr = 0

	while Tcurr < Tmax:
		Crossover(Pop, Pcros)
		Mutation(Pop, Pmut)
		Criteria_new = Values_New + min(Config_New - Config_cur)
		Selection(Pop, Criteria_new)
		Config2 = min_index(Criteria)
		Tcurr += 1

	return Config_New, Criteria(Config_New), min(Config_New - Config_Cur)

	