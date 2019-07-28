# Part 2 of the Python Review lab.

def encode(x, y):
	isprime(x,y)
	if 1 < y < 250 and 500 < x < 1000 :
		return x*y
		coded_message = decode(643,5)

	else: 
		print ("Invalid input: Outside range.")


def isprime(x,y):
	for i in range(2,y):
		if (y % i) == 0:
			print (y, "is not a prime number")
			y+=1
	else: 
		print (y, "is a prime number")

	for i in range(2,x):
		if (x % i) == 0:
			print (x, "is not a prime number")
			y+=1
	else: 
		print (x, "is a prime number")



	



def decode(coded_message):
	return x/y