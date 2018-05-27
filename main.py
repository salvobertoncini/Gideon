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


def fetch_trivial_dataset(trivial_dataset):	
	array_replace = trivial_dataset.split()
	array_json = []
	i=0

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			array_json.append({"id": int(array_replace[i]), "value": array_replace[i+1]})
			
			i+=2

	return array_json


def fetch_raw_dataset(array_json):
	occurrence_json = []
	counter = 0

	for x in array_json:
		found = 0
		for y in occurrence_json:
			if x["id"] == y["id"]:
				found = 1
				y["value"] +=1
				counter += 1
		if found == 0:
			occurrence_json.append({"id": x["id"], "value": 1})
			counter += 1

	occurrence_json.sort(key=operator.itemgetter('id'))

	return occurrence_json, counter


if __name__ == '__main__':
	t0 = time.time()
	dataset_name = 'fire1'
	trivial_dataset = open_file('../datasets/'+dataset_name+'.txt')
	raw_dataset = fetch_trivial_dataset(trivial_dataset)
	json_dataset, len_dataset = fetch_raw_dataset(raw_dataset)
	t1 = time.time()

	#print json.dumps(json_dataset, indent=2)
	print "counter: "+str(len_dataset)
	print "time elapsed: "+str(round(t1-t0, 2))+" seconds"

	#access_control_scheme_design(len_dataset, Tmax, Criteria, Pcros, Pmut)
	#access_control_scheme_reconfig(len_dataset, Tmax, Criteria, Pcros, Pmut, Config_Cur, Values_New)
