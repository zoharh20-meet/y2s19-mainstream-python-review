# Part 3 test of the Python Review lab.

import part4

## Test 1. Tests the init and encode function
print("Test 1")
cipher = part4.Cipher(3,5,1000)
if(cipher.key == 5 and cipher.secret_message = 3):
	print("PASSED")
else:
	print("FAILED")

## Test 2. Tests the init and encode function
print("Test 2")
cipher = part4.Cipher(3,5,1000)
cipher.encode()
if(cipher.coded_message == 15):
	print("PASSED")
else:
	print("FAILED")

## Test 3. Tests the decode function
print("Test 3")
if(part3.decode(15,1000) in [(3,5),(5,3)]): 
	print("PASSED")
else:
	print("FAILED")

## Test 4. Tests the decode function
print("Test 4")
if(part3.decode(4261*1237, 10000) in [(1237,4261),(4261,1237)]): 
	print("PASSED")
else:
	print("FAILED")
