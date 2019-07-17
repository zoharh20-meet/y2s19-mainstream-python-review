# Part 1 test of the Python Review lab.
import part1

## Test 1. Tests the hello_world function
print("Test 1")
if(part1.hello_world() == "hello world"):
	print("PASSED")
else:
	print("FAILED")

## Test 2. Tests the greet_by_name function
print("Test 2")
if(part1.greet_by_name("bob") == "hello bob"):
	print("PASSED")
else:
	print("FAILED")

## Test 3. Tests the encode function
print("Test 3")
if(part1.encode(5) == 5*3953531):
	print("PASSED")
else:
	print("FAILED")

## Test 4. Tests the decode function
print("Test 4")
if(part1.decode(part1.encode(5.5)) == 5.5):
	print("PASSED")
else:
	print("FAILED")