'''
Scenario
Given a Tuple, find out the number of times a string occurs.

Aim
Write a script that uses tuple methods to count the number of elements in a tuple and the number of times a particular element appears in the tuple. Based on these counts, the script will also print a message to the terminal.

Steps for Completion
Initialize a tuple, as shown in Snippet 5.37:
cars = ('coupe', 'coupe', 'coupe', 'carbiolet', 'sedan')
Snippet 5.37

Use a tuple method to count the number of times the coupe element appears in the tuple cars, and assign it to a variable, fav.

Use a tuple method to calculate the length of the tuple cars, and assign it to a variable, amt.

If the number of times the coupe element appears in the tuple cars is more than 45%, print Too many coupes in the garage. to the terminal. If not, print You are all set with cars. to the terminal.
'''

cars = ('coupe','coupe','coupe','carbiolet','sedan')

fav = cars.count("coupe")
amt = len(cars)

if fav / amt > 0.45:
    print("Too many coupes in the garage.")
else:
    print("You are all set with cars.")
