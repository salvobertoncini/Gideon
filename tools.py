def open_file(path):
	#writeLog("file opened: "+path)
	file = open(''+path, 'r')
	file_to_read = file.read()
	file.close()

	return file_to_read


def from_txt_to_dataset(file_name, tag_id, tag_value):
	raw_dataset = open_file(file_name)

	array_replace = raw_dataset.split()
	dataset = []
	i=0

	while i < len(array_replace) - 1:
		if array_replace[i] != ",":
			dataset.append({""+tag_id: int(array_replace[i]), ""+tag_value: array_replace[i+1]})
			
			i+=2

	return dataset
