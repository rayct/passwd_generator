# Generate Secure Random Passwords and Tokens in Python
## In this piece, I learned the proper ways to generate strong random passwords and tokens that are cryptographically secured.
## Having secure random numbers allows us to manage sensitive information, such as password and security tokens.
## We will be using the secrets module, available since Python 3.6. The official documentation states:

## “… secrets should be used in preference to the default pseudo-random number generator in the random module,
## which is designed for modelling and simulation, not security or cryptography.”

## There are three sections in this article:

### Basic Usage
### Examples
### Conclusion

##  1. Basic Usage
### The secrets module provides a few built-in functions that we can use to generate numbers and tokens.
### No setup was required but I needed to import the module before I can use it.

##  2. Examples
### In this section, I will outline some of the best practices for generating a secure password and token.
### Feel free to test them on your own.
### Generate a 10-characters alphanumeric password


##  3. Conclusion
### A recap what we’ve learned today.
### I started off exploring the basic functions provided by the secrets module.
### Then, I tested the functions to generate some random password and tokens in string token or bytes.
### Finally, I tried to play with the module and generated a few different types of password that are strong and secured.
### Also I learned that you should not store your password in any plain text or encrypted file that is easily recoverable.
### They should be salted and hashed using an irreversible, one-way hash function.

### Finally A big Thank you to #clcoding.com for providing this short nugget of tech gold.

### #rayturner.dev