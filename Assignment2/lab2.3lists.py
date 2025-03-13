'''
Scenario
Write a program that fetches the first count amount of elements of a list.

Aim
Create a script that contains the array [34, 9, 32, 91, 58, 13, 77, 21, 56]. The script will take a user input count that defines the number of elements to fetch from an array and then outputs those elements.

Steps for Completion
Go to your main.py file.

On the first line, create the following array:

numbers = [34, 9, 32, 91, 58, 13, 77, 21, 56]
Next, print the array numbers and fetch the user input count for the number of elements to fetch from the array.

Finally, print out the slice of the array from the first element to the nth element.

Then, run the script by using the python3 main.py command
'''

numbers = [34, 9, 32, 91, 58, 13, 77, 21, 56]
print("Numbers:", numbers)

userInt = int(input("Number of elements to fetch from array: "))

fetchedNum = numbers[:userInt]
print(fetchedNum)
