import time

def start_timer():
	t0 = time.time()

	return t0

def end_timer(t0):
	t1 = time.time()

	print "time elapsed: "+str(round(t1-t0, 3))+" seconds"
