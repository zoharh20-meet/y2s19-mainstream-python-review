# Part 3 test of the Python Review lab.

import part3

## Test 1. Tests the createShiftDictionary function
print("Test 1")
if(part3.createShiftDictionary(3)['z'] == 'c'):
	print("PASSED")
else:
	print("FAILED")

## Test 2. Tests the encode function
print("Test 2")
if(part3.encode('hi students, how are you?', 7) == 'op zabkluaz, ovd hyl fvb?'):
	print("PASSED")
else:
	print("FAILED")

## Test 3. Tests the decode function
print("Test 3")
if(part3.decode('op zabkluaz, ovd hyl fvb?', 7) == 'hi students, how are you?'):
	print("PASSED")
else:
	print("FAILED")

## Test 4. Tests the decode function
print("Test 4")
if('hi students, how are you?' in part3.decodeAll('op zabkluaz, ovd hyl fvb?')):
	print("PASSED")
else:
	print("FAILED")