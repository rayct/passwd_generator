import secrets
# Generate a random number
# Use the randbelow function to generate a number.
# It accepts an integer and the number generated is between 0 and the input integer minus 1.
# The input integer must be higher than 0
secrets.randbelow(2) # generate either 0 or 1
secrets.randbelow(10) # generate a number from 0 to 9
secrets.randbelow(0) # error
secrets.randbelow(-10) # error



# You can also use the randbits function to generate a random number.
# It accepts an integer which represents the number of bits.
# The input integer must be higher than 0.
secrets.randbits(1) # generate either 0 or 1
secrets.randbits(2) # generate a number from 0 to 3
secrets.randbits(4) # generate a number from 0 to 15
secrets.randbits(8) # generate a number from 0 to 255



# Generate a random element from a list
# The module also provides a way for us to choose a random element from a non-empty sequence.
# Let’s try it out using the choice function

colour = ['red', 'blue', 'green', 'purple', 'yellow']
secrets.choice(colour)
# Generate a random byte string
# token_bytes function is the perfect choice for generating bytes. 
# You can specify an integer as a parameter.
# It will determine a random integer if you don’t specify anything.
secrets.token_bytes(8) # generate 8 random bytes string
# You should see a random byte string like this:
# b'\x1bq\x8e\x83\x08\xb2g\x17



# Generate a random string in hexadecimal
# If you wanted a string in hexadecimal, you can use the token_hex function.
# Just like the token_bytes function, it accepts an integer which is used to generate n number of bytes,
# each byte will be converted to two hex digits later.
secrets.token_hex(16) # generate 16 random hexadecimal string
# This is an example of the output:
# cd7b7fb7e0c5c1fa17389050f884526e



# Generate a URL-safe string
# Sometimes, you might want a string that is Base64 encoded for your web application.
# The token_urlsafe function comes in handy for such a use case.
secrets.token_urlsafe(16)
# I got the following result:
# S357dE8QSuE



# 2. Examples
# In this section, I will outline some of the best practices for generating a secure password and token.
# Feel free to test them on your own.
# Generate a 10-characters alphanumeric password
import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(10))
print(password)
# `ascii_letters` — contains both the lower case and upper case from A-Z



# Generate a 10-characters hexadecimal password with punctuation
import string
import secrets
alphabet = string.hexdigits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(10))
print(password)

# Generate a 10-characters password with at least one lowercase, one uppercase, and one digit
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
        break
print(password)

# `islower` — Determine if the character is lowercase
# `isuppe` — Determine if the character is uppercase
# `isdigit` — Determine if the character is a digit

# Generate a 10-characters password with at least two uppercase and two digits
import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (sum(c.isupper() for c in password) >= 2 and sum(c.isdigit() for c in password) >= 2):
        break
print(password)

# Generate a four-word password that is unique
import secrets
animal = ['horse', 'elephant', 'monkey', 'donkey', 'goat', 'chicken', 'duck', 'mouse']
fruit = ['apple', 'banana', 'peach', 'orange', 'papaya', 'watermelon', 'durian']
electronic = ['computer', 'laptop', 'smartphone', 'battery', 'charger', 'cable']
vegetable = ['lettuce', 'spinach', 'celery', 'cabbage', 'turnip', 'cucumber', 'eggplant']
word_list = animal + fruit + electronic + vegetable
password = set()
while True:
    password.add(secrets.choice(word_list))
    if(len(password) >= 4):
        break
print(' '.join(password))

# Generate a temporary URL with security tokens for a password reset
import secrets
url = 'https://mywebsite/reset?key=' + secrets.token_urlsafe()
print(url)


# 3. Conclusion
# A recap what we’ve learned today.
# I started off exploring the basic functions provided by the secrets module.
# Then, I tested the functions to generate some random password and tokens in string token or bytes.
# Finally, I tried to play with the module and generated a few different types of password that are strong and secured.
# Also I learned that you should not store your password in any plain text or encrypted file that is easily recoverable.
# They should be salted and hashed using an irreversible, one-way hash function.