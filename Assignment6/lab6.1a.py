'''
Aim
We will create a dictionary and verify its type.

Steps for Completion
Go to the main.py file.

Use the dict function or curly bracket notation to create a dictionary and assign it to a variable, location.

Within a print function, use the built-in type function on location to see if it is an instance of the dict class.

A typical example of a dictionary is shown in Snippet 6.5:

location = dict(
	state="CA",
	city="Los Angeles"
)
Snippet 6.5

In this example, state and city are keys, while CA and Los Angeles are the respective values assigned to them.
'''

location = dict(
	state="CA",
	city="Los Angeles"
)

print(type(location))