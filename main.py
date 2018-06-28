#Personal import
import evaluator
import generator
import genetic_algorithm
import tools


if __name__ == '__main__':
	dataset_name = 'hc'
	file_name = 'datasets/'+dataset_name+'.txt'

	t0 = evaluator.start_timer()

	#Number of individuals in population
	Npop = 200
	#Max number of iterations i.e. at least 10
	Tmax = 1
	#Probability of crossover
	Pcros = 10
	#Probability of mutation
	Pmut = 10

	#Fitness function parameters, w1 << w2
	w1 = 1
	w2 = 10

	#obtain initial matrix Sreq, the number of user h and the number of permission w
	Sreq, h, w, UPA, DENSITY = generator.from_txt_to_matrix(file_name)

	#Creation of the initial population, h < w
	Population = generator.Population_creation(Npop, h, w)

	Config = genetic_algorithm.access_control_schema(Sreq, h, w, Population, Npop, Tmax, Pcros, Pmut, w1, w2)

	evaluator.end_timer(t0)

	#print and testing
	print "********************************************************"
	print Config[0]

	"""
	USERS represents the number of users in the organization. 
	PRMS represents the total number of permissions. 
	UPA is the total number of permissions assigned to all the users in the given system.
	DUPA is the total number of permissions assigned to all the users in the resultant system.
	DENSITY represents what percentage of total assignable permissions is actually assigned to the users of the system in the UPA.
	"""

	ROLES = evaluator.how_many_roles(Config[0])
	PA = evaluator.how_many_elements_in_PA(Config)
	UA = evaluator.how_many_elements_in_UA(Config)

	S1 = UA + PA
	S2 = S1 + ROLES

	DUPA = evaluator.density_DUPA(h, w, Config)

	print "********************************************************"
	print "roles: "+str(ROLES)
	print "users: "+str(h)
	print "permissions: "+str(w)
	print "PA: "+str(PA), "UA: "+str(UA)
	print "DUPA: "+str(DUPA), "UPA: "+str(UPA), "DUPA/UPA: "+str(DUPA*100/UPA)+"%"
	print "density: "+str(DENSITY)+"%"
