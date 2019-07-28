# Part 1 of the Python Review lab.

def hello_world():
	return ("hello world")

hi= hello_world()

def greet_by_name(name):
	return ("hello"+ " "+name)
greeting = greet_by_name("bob")

def encode(x):
	return (x * 3953531)
result = encode(5)

def decode(x):
	return  (x/3953531)
result2 = decode (result)
print(result, result2)
	
