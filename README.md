## Y2 2018 Summer: Python Review Lab

Welcome to the Python review lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Part 1: Basic functions

The stubs for these functions can be found in `part1.py`. You can test your functions by running `part1-test.py`.

1. Write a function to `hello_world`, which takes in no inputs
and prints `hello world`. 

2. Write a function `greet_by_name` which takes in a string, `name`,
and prints `hello <name>`

3. Write a function, `encode`, that takes in a number, `x` and computes
the product of `x` and 3953531.
This function shouldn't print anything, but should return an integer value.

4. Write a function, `decode`, which takes in the output from the previous function and
finds `x`. You may use the value 3953531 in this function.

5. Test your `encode` and `decode` functions to make sure that they work. To do this, try to run `decode(encode(x))` and make sure you get your original value of `x`!

### Part 2: Loops

The stubs for these functions can be found in `part2.py`.

1. First, update your function `encode`, to take in 2 numbers `x` and `y`, and compute their product.
This function should require `1 < y < 250` and `500 < x < 1,000`. If this isn't true, the function should print
`Invalid input: Outside range.`, and return None.

2. Update your encode function to guarantee that the inputs `x` and `y` are prime. If `x` is not prime,
then keep incrementing the value of `x` until it is prime; then, do the same process for `y`. If this
causes the new values of `x` and `y` to be out of the range, print `Invalid input: Outside range.`,
and return None.  
*Hint: Have we implemented any functions previously, which could be useful here?*

3. Write a function, `decode`, which takes in the output (the value of the product)
from your updated `encode` function and tries to compute values for `x` and `y`.
This function only takes in, as input,
the `coded_message`, which is output from `encode`. You may also use the ranges of possible values for `x` and `y` - that is, `1 < y < 250` and `500 < x < 1,000`.
Consider trying all possible values for `x` and `y`!
*Hint: The mod function might be useful here! The mod function can be used to calculate the remainder.
For instance, `500 % 6` returns the remainder when 500 is divided by 6.*

4. A good programmer always writes test cases! Test your `encode` and `decode` functions to
make sure they work in `part2-test.py`. Make sure to include test cases for all possible cases of x and y. Note that the `encode` function changes your input to make sure that it's prime. Thus, if your original input was not prime, `decode(encode(x, y))`, might not return the original values of `x` and `y`. Make sure you account for this when writing test cases.

### Part 3: Classes

The stubs for these functions can be found in `part3.py`.

= The `encode` and `decode` functions that you've constructed before are the basics of cryptography, the science
of creating and breaking codes. Now, to make things trickier, we want to create a class of codes.

1. Start by creating a class, `Cipher`, which has the following attributes, when
initialized:
- `secret_message`: a number we're trying to hide (the access code to the treasure..)
- `key`: the number we're using to hide our message (the number we multiply by!)
- `limit`: An integer representing the maximum value that the key or message can have. We assume
that all keys and messages must be non-negative.
Example: 1000

2. When initializing, make sure that both the `key` and `secret_message` values are greater than 1.
If they are, print `Invalid input: Keys and messages must be greater than one.` Similarly, make sure that
both the `key` and `secret_message` values are prime. If they are not, print `Invalid input: Both key
and message must be prime.`

3. Instead of initializing the Cipher class with explicit key and message limits, provide a
default value for the `limit` attribute of 10,000. If the key or the secret_message violates the limit,
then print `Invalid input: Keys and messages must be at most the limit, which is <LIMIT>.`

4. Add a function `encode`, which multiplies the `secret_message` by the `key`
to get the coded message. Now, instead of printing the coded message,
add it as a new attribute in the class named `coded_message`!

5. Now, create a new class `Decoder`, which has the following attributes, when 
initialized:
- `coded_message`: the product of two large prime numbers
- `limit`: the maximum value that the key or message can have.

6. Now, add a `decode` function, to this class, to decode the `coded_message`. 
We can see how secure our system is by checking how long it takes us to decode! This function
should return a tuple of the form `(key, secret_message)`.
*Note: Order isn't important here. The tuples (5, 135) and (135, 5) are the same
thing*

7. Finally, test that your functions are working properly, by choosing some primes and making sure your classes return the expexted values

8. Run part4-test.py to check your code further.

Bonus 9. Instead of initializing the Cipher class with a key, update the class
so it's just initialized with the `secret_message`. Then, write a function to randomly choose a
key value within the range `1 < key < limit`. This function should be called immediately after initialization and update the key attribute of your class. Note that this function should repeatedly choose a random value, until a value
which is prime is chosen.
Hint: Consider using the `random` module, in Python for this!

### BONUS:

Read about Vignere ciphers here: http://www.crypto-it.net/eng/simple/vigenere-cipher.html?tab=1.

Implement Vignere cipher encode and decode functions. Remember that your encode function must take in both a plaintext string and a keyword. Make sure your keyword is short (less than 10 characters). Your decode function should also take in a ciphertext string and a keyword. Also, be sure to write test cases for your functions!

Alternatively, research and implement a different cipher of your choice.