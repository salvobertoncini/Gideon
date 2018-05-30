#Generator
import tools
import operator


def build_dataset(dataset_name, tag_id, tag_value):
	tools.writeLog("build_dataset")
	trivial_dataset = tools.open_file('../datasets/'+dataset_name+'.txt')
	raw_dataset = fetch_trivial_dataset(trivial_dataset, tag_id, tag_value)

	mapped_json = mapping_dataset_x_y(raw_dataset, tag_id, tag_value)
	#print mapped_json

	dataset, Npop = fetch_raw_dataset(raw_dataset, tag_id, tag_value)

	return dataset, Npop


def chromosomes_convertion(dataset, tag_id):
	tools.writeLog("chromosomes_convertion")
	population = []

	for x in dataset:
		population.append(str(dec_to_bin(x[""+tag_id])))

	return population


def create_population(pop_size):
	tools.writeLog("create_population")
	population = []
	for x in range(pop_size):
		chromosome = str(dec_to_bin(random.randint(0, 512)))
		population.append(chromosome)

	return chromosomes_normalization(population)


def dec_to_bin(x):
    return int(bin(x)[2:])


def fetch_raw_dataset(array_json, tag_id, tag_value):
	tools.writeLog("fetch_raw_dataset")
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


def fetch_trivial_dataset(trivial_dataset, tag_id, tag_value):
	tools.writeLog("fetch_trivial_dataset")	
	array_replace = trivial_dataset.split()
	array_json = []
	i=0

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			array_json.append({""+tag_id: int(array_replace[i]), ""+tag_value: array_replace[i+1]})
			
			i+=2

	return array_json


def load_dataset_process(dataset_name, tag_id, tag_value):
	tools.writeLog("load_dataset_process "+dataset_name)
	dataset, Npop = build_dataset(dataset_name, ''+tag_id, ''+tag_value)
	#print_dataset(dataset_name, Npop, dataset)
	population = chromosomes_convertion(dataset, ''+tag_id)

	return population


def mapping_dataset_x_y(dataset, tag_id, tag_value):
	tools.writeLog("mapping_roles_permissions")
	mapped_json = []

	for x in dataset:
		found = 0
		for y in mapped_json:
			if x[""+tag_id] == y[""+tag_id]:
				found = 1
				y[""+tag_value].append(x[""+tag_value])
		if found == 0:
			list_tmp = []
			list_tmp.append(x[""+tag_value])
			mapped_json.append({""+tag_id: x[""+tag_id], ""+tag_value: list_tmp})

	mapped_json.sort(key=operator.itemgetter(''+tag_id))
	
	return mapped_json

