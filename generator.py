import random

def list_of_tag(dataset, tag):
	list_tag = []

	for x in dataset:
		if x[""+tag] not in list_tag:
			list_tag.append(x[""+tag])

	return list_tag

def Individual_creation(x_list):
	Individual = ""

	#Creation of chromosomes which lenght is the number of users or permissions
	for i in range(0,len(x_list)):
		Individual += str(random.randint(0, 1))

	return Individual


def create_population(dataset, Npop, tag_id, tag_value):
	users_list = list_of_tag(dataset, tag_id)
	permissions_list = list_of_tag(dataset, tag_value)

	X = []
	Y = []
	Population = []

	for i in range(0,Npop):
		X = (Individual_creation(users_list))
		Y = (Individual_creation(permissions_list))
		Population.append([X, Y])

	return Population