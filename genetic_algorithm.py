#Genetic Algorithm
import random
import tools


def f_first(x):
	tools.writeLog("f_first")
	lenght = len(x)
	return x[0:lenght]


def f_second(x):
	tools.writeLog("f_second")
	lenght = len(x)
	return x[lenght:len(x)]


def crossover(population, Pcros):
	tools.writeLog("crossover")
	x_population = []
	Npop = len(population)
	Num_Op = Npop * Pcros

	for i in range(Num_Op):

		if Pcros > random.randint(0, 100):
			first = random.choice(population)
			second = random.choice(population)

			x = f_first(first)
			y = f_second(second)
			z = x+y
			x_population.append(z)

	return tools.chromosomes_normalization(x_population)


def mutation(population, mutation_percentage):
	tools.writeLog("mutation")
	x_population = []
	for chromosome in population:
		alea = 0
		i = 0
		while i < len(chromosome):
			x_chromosome = list(chromosome)
			while alea == 0:
				if mutation_percentage > random.randint(0, 100):
					alea = 1
					if x_chromosome[i] == '0':
						x_chromosome[i] = '1'
					else:
						x_chromosome[i] = '0'

			x_population.append(''.join(x_chromosome))
			i += 1

	return x_population


def selection(population, crossovered_population, mutated_population):
	tools.writeLog("selection")
	#population = tools.remove_duplication(population)

	Npop = len(population)
	population.extend(crossovered_population)
	population.extend(mutated_population)

	population = tools.remove_duplication(population)
	i_max = len(population)

	#fitness function
	#population = Sort(population, F)

	i = Npop

	#print "i: "+str(i)+", i_max: "+str(i_max)

	while i < i_max:
		x = population[i]
		population.remove(x)
		i += 1
		i_max -= 1

	return population


def access_control_scheme_design(population, Tmax, Pcros, Pmut):
	tools.writeLog("access_control_scheme_design")
	after_selection_population = []

	# iteration from 0 to Tmax
	for x in range(0, Tmax):
		print "stage "+str(x+1)
		#crossover
		crossovered_population = crossover(population, Pcros)
		#mutation
		mutated_population = mutation(population, Pmut)
		#selection
		after_selection_population = selection(population, crossovered_population, mutated_population)

	#return tools.remove_duplication(after_selection_population)
	return after_selection_population

