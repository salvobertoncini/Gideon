# general import
import json
import operator
import time

# personal import
import access_control_scheme_reconfig
import access_control_scheme_design


def open_file(path):
	file = open(''+path, 'r')
	#logs = open('log', 'w') 
	file_to_read = file.read()
	file.close()

	return file_to_read

def print_dataset(dataset):
	print json.dumps(dataset, indent=2)

def fetch_trivial_dataset(trivial_dataset, tag_id, tag_value):	
	array_replace = trivial_dataset.split()
	array_json = []
	i=0

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			array_json.append({""+tag_id: int(array_replace[i]), ""+tag_value: array_replace[i+1]})
			
			i+=2

	return array_json


def fetch_raw_dataset(array_json):
	occurrence_json = []
	population_counter = 0

	for x in array_json:
		found = 0
		for y in occurrence_json:
			if x["user"] == y["user"]:
				found = 1
				y["population_counter"] +=1
		if found == 0:
			occurrence_json.append({"user": x["user"], "population_counter": 1})
		
		population_counter += 1

	occurrence_json.sort(key=operator.itemgetter('user'))

	return occurrence_json, population_counter


if __name__ == '__main__':
	t0 = time.time()
	dataset_name = 'domino'
	trivial_dataset = open_file('../datasets/'+dataset_name+'.txt')
	raw_dataset = fetch_trivial_dataset(trivial_dataset, 'user', 'resource')
	json_dataset, Npop = fetch_raw_dataset(raw_dataset)
	t1 = time.time()

	print_dataset(raw_dataset)
	#print_dataset(json_dataset)

	print "dataset: "+dataset_name
	print "population: "+str(Npop)
	print "time elapsed: "+str(round(t1-t0, 2))+" seconds"

	#access_control_scheme_design(Npop, Tmax, Criteria, Pcros, Pmut)
	#access_control_scheme_reconfig(Npop, Tmax, Criteria, Pcros, Pmut, Config_Cur, Values_New)
