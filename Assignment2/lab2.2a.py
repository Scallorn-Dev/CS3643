'''
Scenario
You will create a Python script that will take a user's input and convert lower case letters in the string into upper case letters depending on the user input.

Aim
Write a script that converts the count amount of letters starting from the end of a given word to uppercase. The script should take the word as a string and specify the count amount of letters to convert as an integer input from the user. You can assume that the count variable will be a positive number.

Steps for Completion
Open your main.py file.

On the first line, request the string to convert from the user.

On the next line, request how many letters at the end of the word should be converted, cast the input to type int and save their input to a variable named count.

Next, get the start of the string.

Then, get the ending of the string, that is, the one we'll be converting.

Then, concatenate the first and last part back together, with the last substring transformed.

Finally, run the script with the python3 main.py command
'''

userStr = input("Word to convert: ")

count = int(input("How many letters at the end of the word should be converted? "))

startingPos = userStr[:-count] if count < len(userStr) else ''

endPos = userStr[-count:].upper()

addConversion = startingPos + endPos

print(addConversion)
