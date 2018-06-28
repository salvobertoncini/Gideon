#General import
import time

#Personal import
import tools


def start_timer():
	return time.time()


def end_timer(t0):
	print "time elapsed: "+str(round(time.time() - t0, 3))+" seconds"


def how_many_roles(Individual):
	return sum(gene > 0 for gene in Individual[0])


def how_many_elements_in_UA(Population):
	return sum( sum(gene > 0 for gene in Individual[0]) for Individual in Population)
	

def how_many_elements_in_PA(Population):
	return sum( sum(gene > 0 for gene in Individual[1]) for Individual in Population)

def density_DUPA(h, w, Population):
	DUPA = 0
	
	Population = tools.from_lists_to_binary_matrix(Population)

	Individual = Population[0]
	for i in range(0, h):
		for j in range(0, w):
			k_iter = len(Individual[0])
			k_sum = 0
			for k in range (0, k_iter):
				x = bool(Individual[0][k][i])
				y = bool(Individual[1][k][j])

				k_sum = k_sum | x & y

			if k_sum == 1:
				DUPA+=1

	return DUPA

