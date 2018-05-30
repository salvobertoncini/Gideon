#Evaluator
import time

def start_time():
	t0 = time.time()

	return t0

def end_time(t0):
	t1 = time.time()

	print "time elapsed: "+str(round(t0-t1, 3))+" seconds"
