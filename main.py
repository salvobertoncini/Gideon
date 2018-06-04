#Personal import
import evaluator
import generator
import genetic_algorithm
import tools

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

	dataset = tools.from_txt_to_dataset(file_name, tag_id, tag_value)
	population = generator.create_population(dataset, Npop, tag_id, tag_value)

	config = genetic_algorithm.access_control_scheme_design(population, Npop, Tmax, Pcros, Pmut)

	evaluator.end_timer(t0)

	#print matrix
	#print config[0]
