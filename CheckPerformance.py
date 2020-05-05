#Decorator
from time import time


def performance(ftn):
	def wrapper(*args,**kawrgs):
		t1=time()
		result = ftn(*args,**kawrgs)
		t2=time()
		print(f'took {t2-t1} ms')
		return result
	return wrapper
		
@performance
def long_time():
	for i in range(10000000):
		i*5

long_time()