#Tools
import datetime


def open_file(path):
	writeLog("file opened: "+path)
	file = open(''+path, 'r')
	file_to_read = file.read()
	file.close()

	return file_to_read


def print_dataset(dataset_name, Npop, dataset):
	writeLog("print_dataset")
	print "dataset: "+dataset_name+", population: "+str(Npop)
	#print json.dumps(dataset, indent=2)


def remove_duplication(population):
	writeLog("remove_duplication")
	return list(set(population))


def writeLog(message):
	log = open('log.txt', 'a')
	log.write(str(datetime.datetime.now()) +" - "+message + "\n")
	log.close()


def chromosomes_normalization(population):
	writeLog("chromosomes_normalization")
	x_population = []
	max_length,longest_element = max([(len(x),x) for x in population])

	for chromosome in population:
		while len(chromosome) < max_length:
			chromosome = ''.join(('0', chromosome))

		x_population.append(''.join(chromosome)) 

	return x_population

