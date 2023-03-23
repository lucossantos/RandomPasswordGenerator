import string
import random


def generate_password(length):
	# Define the characters to use in the password
	chars = string.ascii_letters + string.digits + string.punctuation

	# Generate a random password of the specified length
	password = ''.join(random.choice(chars) for i in range(length))

	return password


# Test the function
password = generate_password(12)
print(password)