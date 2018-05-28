# general import
import json
import operator
import time
import datetime
import random

# personal import
#import genetic_tools
#import access_control_scheme_reconfig
#import access_control_scheme_design


def open_file(path):
	file = open(''+path, 'r')
	file_to_read = file.read()
	file.close()

	return file_to_read


def writeLog(message):
	log = open('log.txt', 'a')
	log.write(str(datetime.datetime.now()) +" - "+message + "\n")
	log.close()


def print_dataset(dataset_name, Npop, dataset):
	print "dataset: "+dataset_name+", population: "+str(Npop)
	#print json.dumps(dataset, indent=2)


def fetch_trivial_dataset(trivial_dataset, tag_id, tag_value):	
	array_replace = trivial_dataset.split()
	array_json = []
	i=0

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			array_json.append({""+tag_id: int(array_replace[i]), ""+tag_value: array_replace[i+1]})
			
			i+=2

	return array_json


def fetch_raw_dataset(array_json, tag_id, tag_value):
	occurrence_json = []
	population_counter = 0

	for x in array_json:
		found = 0
		for y in occurrence_json:
			if x[""+tag_id] == y[""+tag_id]:
				found = 1
				y["population_counter"] +=1
		if found == 0:
			occurrence_json.append({""+tag_id: x[""+tag_id], "population_counter": 1})
		
		population_counter += 1

	occurrence_json.sort(key=operator.itemgetter(''+tag_id))

	return occurrence_json, population_counter


def build_dataset(dataset_name, tag_id, tag_value):
	trivial_dataset = open_file('../datasets/'+dataset_name+'.txt')
	raw_dataset = fetch_trivial_dataset(trivial_dataset, tag_id, tag_value)
	dataset, Npop = fetch_raw_dataset(raw_dataset, tag_id, tag_value)

	return dataset, Npop


def dec_to_bin(x):
    return int(bin(x)[2:])


def chromosomes_convertion(dataset, tag_id):
	population = []

	for x in dataset:
		population.append(str(dec_to_bin(x[""+tag_id])))

	return population


def create_population(pop_size):
	population = []
	for x in range(pop_size):
		chromosome = str(dec_to_bin(random.randint(0, 512)))
		population.append(chromosome)

	return chromosomes_normalization(population)


def f_first(x):
	lenght = len(x)
	return x[0:lenght]


def f_second(x):
	lenght = len(x)
	return x[lenght:len(x)]


def crossover(population, Pcros):
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

	return chromosomes_normalization(x_population)


def chromosomes_normalization(population):
	x_population = []
	max_length,longest_element = max([(len(x),x) for x in population])

	for chromosome in population:
		while len(chromosome) < max_length:
			chromosome = ''.join(('0', chromosome))

		x_population.append(''.join(chromosome)) 

	return x_population


def mutation(population, mutation_percentage):
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
	population = remove_duplication(population)

	Npop = len(population)
	population.extend(crossovered_population)
	population.extend(mutated_population)

	population = remove_duplication(population)
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


def remove_duplication(population):
	return list(set(population))


def access_control_scheme_design(population, Tmax, Pcros, Pmut):
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

	return remove_duplication(after_selection_population)


if __name__ == '__main__':
	
	#managing dataset
	t0 = time.time()
	
	resources_dataset_name = 'fire1'
	writeLog("build_dataset "+resources_dataset_name)
	resources_dataset, resources_Npop = build_dataset(resources_dataset_name, 'resource', 'role')
	
	users_dataset_name = 'fire2'
	writeLog("build_dataset "+ users_dataset_name)
	users_dataset, users_Npop = build_dataset(users_dataset_name, 'user',  'role')

	print_dataset(resources_dataset_name, resources_Npop, resources_dataset)
	print_dataset(users_dataset_name, users_Npop, users_dataset)
	
	population1 = chromosomes_convertion(resources_dataset, 'resource')
	population2 = chromosomes_convertion(users_dataset, 'user')

	t1 = time.time()
	print "time elapsed: "+str(round(t1-t0, 3))+" seconds"

	#create random population
	t0 = time.time()

	#maximal number of iterations
	Tmax = 10
	#probability of crossover
	Pcros = 15
	#probability of mutation
	Pmut = 10

	#Number of individuals in population
	#Npop = 150
	Npop = users_Npop if users_Npop > resources_Npop else resources_Npop

	random_population = create_population(Npop)

	population = access_control_scheme_design(random_population, Tmax, Pcros, Pmut)

	print sorted(population)
	#print sorted(after_selection_population)

	t1 = time.time()
	print "time elapsed: "+str(round(t1-t0, 3))+" seconds"


	#access_control_scheme_design(Npop, Tmax, Criteria, Pcros, Pmut)
	#access_control_scheme_reconfig(Npop, Tmax, Criteria, Pcros, Pmut, Config_Cur, Values_New)
