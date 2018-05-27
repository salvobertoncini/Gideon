# general import
import json
import operator
import time
import datetime

# personal import
import genetic_tools
import access_control_scheme_reconfig
import access_control_scheme_design


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


if __name__ == '__main__':
	t0 = time.time()

	resources_dataset_name = 'fire1'
	writeLog("build_dataset "+resources_dataset_name)
	resources_dataset, resources_Npop = build_dataset(resources_dataset_name, 'user',  'role')
	

	users_dataset_name = 'fire2'
	writeLog("build_dataset "+ users_dataset_name)
	users_dataset, users_Npop = build_dataset(users_dataset_name, 'role', 'resource')

	t1 = time.time()

	print_dataset(resources_dataset_name, resources_Npop, resources_dataset)
	print_dataset(users_dataset_name, users_Npop, users_dataset)

	print "time elapsed: "+str(round(t1-t0, 2))+" seconds"

	#access_control_scheme_design(Npop, Tmax, Criteria, Pcros, Pmut)
	#access_control_scheme_reconfig(Npop, Tmax, Criteria, Pcros, Pmut, Config_Cur, Values_New)
