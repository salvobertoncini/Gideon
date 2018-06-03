#Generator
import operator
import random
import tools
import json


def how_many_roles(dataset, tag_id, tag_value):
	tag_id_list = []
	tag_value_list = []

	for x in dataset:
		for y in x[""+tag_value]:
			if y not in tag_value_list:
				tag_value_list.append(y)
		if x[""+tag_id] not in tag_id_list:
			tag_id_list.append(x[""+tag_id])

	return len(tag_value_list), len(tag_id_list)


def how_many_permissions(dataset, tag_value):
	tag_value_list = []

	for x in dataset:
		found = 0
		for z in tag_value_list:
			if y == x[""+tag_value]:
				found = 1
		if found == 0:
			tag_value_list.append(x[""+tag_value])

	#tag_value_list.sort(key=operator.itemgetter(''+tag_value))
	#tag_value_list.sort()

	return tag_value_list


def build_dataset(dataset_name, tag_id, tag_value):
	tools.writeLog("build_dataset")
	trivial_dataset = tools.open_file('../datasets/'+dataset_name+'.txt')
	raw_dataset = fetch_trivial_dataset(trivial_dataset, tag_id, tag_value)

	dataset = mapping_dataset_x_y(raw_dataset, tag_id, tag_value)

	#dataset = fetch_raw_dataset(raw_dataset, tag_id, tag_value)

	return dataset, len(dataset)


def chromosomes_convertion(dataset, tag_id):
	tools.writeLog("chromosomes_convertion")
	population = []

	for x in dataset:
		population.append(str(dec_to_bin(x[""+tag_id])))

	return population


def create_chr_Z(Npop):
	chr_Z = []
	#Npop = len(population1) if len(population1) > len(population2) else len(population2)
	for x in range(0, Npop):
		chr_Z.append(1)

	return chr_Z


def create_role_matrix(dataset, max_limit, tag_id):
	x, y = how_many_roles(dataset)
	max_limit = x/y
	permission_max_limit = how_many_permissions(dataset, tag_value)


	w = len(dataset)
	h = permission_max_limit

	chr_X = tools.create_matrix(w, h)

	for i in range(0, w):
		for j in range(0, h):
			chr_X[i][j] = str(dec_to_bin(random.randint(0, max_limit)))

	return chr_X


def create_population(dataset, tag_id, tag_value):
	x, y = how_many_roles(dataset, tag_id, tag_value)
	roles_max_limit = x/y

	max_limit = 512

	#creare array di ruoli casuali
	#how_many_roles(dataset)

	#per chr_X si deve avere la lista degli utenti, e mappare i ruoli agli utenti casualmente
	#create_role_matrix(dataset, permission_max_limit, tag_id)
	
	#per chr_Y si deve avere la lista dei permessi, e mappare i ruoli ai permessi casualmente
	#create_role_matrix(dataset, permission_max_limit, tag_value)


	tools.writeLog("create_population")
	population = []

	#user
	w = y
	h = roles_max_limit
	chr_X = tools.create_matrix(w, h)

	#permission
	w = x
	h = roles_max_limit
	chr_Y = tools.create_matrix(w, h)

	chr_Z = create_chr_Z(roles_max_limit)

	for x in range(0, len(dataset)):
		#chromosome = { chr_X, chr_Y, chr_Z }
		chromosome = str(dec_to_bin(random.randint(0, max_limit)))
		population.append(chromosome)

	tools.chromosomes_normalization(population)

	return population


def dec_to_bin(x):
    return int(bin(x)[2:])


def fetch_raw_dataset(array_json, tag_id, tag_value):
	tools.writeLog("fetch_raw_dataset")
	occurrence_json = []

	for x in array_json:
		found = 0
		for y in occurrence_json:
			if x[""+tag_id] == y[""+tag_id]:
				found = 1
				y["population_counter"] +=1
		if found == 0:
			occurrence_json.append({""+tag_id: x[""+tag_id], "population_counter": 1})

	occurrence_json.sort(key=operator.itemgetter(''+tag_id))

	return occurrence_json


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
	tools.print_dataset(dataset_name, Npop, dataset)
	#population = chromosomes_convertion(dataset, ''+tag_id)
	return dataset


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

