# general import

# personal import
import generator
import genetic_algorithm
import evaluator
import tools
#import genetic_tools
#import access_control_scheme_reconfig
#import access_control_scheme_design


if __name__ == '__main__':
	#managing dataset
	t0 = evaluator.start_timer()
	
	dataset_name = 'domino'
	population1 = generator.load_dataset_process(dataset_name, 'resource', 'role')

	dataset_name = 'fire1'
	population2 = generator.load_dataset_process(dataset_name, 'user', 'role')

	evaluator.end_timer(t0)

	#create random population
	t1 = evaluator.start_timer()

	#maximal number of iterations
	Tmax = 3
	#probability of crossover
	Pcros = 15
	#probability of mutation
	Pmut = 10

	#Number of individuals in population
	#Npop = 150
	Npop = len(population1) if len(population1) > len(population2) else len(population2)

	population = population1 if len(population1) > len(population2) else population2
	#population = create_population(Npop)

	population = genetic_algorithm.access_control_scheme_design(population, Tmax, Pcros, Pmut)
	#access_control_scheme_design(Npop, Tmax, Criteria, Pcros, Pmut)
	#access_control_scheme_reconfig(Npop, Tmax, Criteria, Pcros, Pmut, Config_Cur, Values_New)

	print sorted(population)
	print "population: "+str(len(population))
	
	evaluator.end_timer(t1)

