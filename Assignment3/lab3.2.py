'''
Aim
We have recently walked through a simple if statement block that results to a value based on the input given. The script is shown again in Snippet 3.11:

python3_year = 2008
year = int(input('When was Python3 first released?'))

if year == python3_year:
    print('That is correct.')
elif year > python3_year:
    print('Incorrect, too late.')
elif year < python3_year:
	print('Incorrect, too early.')
print('Have a great day!')
Snippet 3.11

Modify this block as follows:

• The user prompt should be Return TRUE or FALSE: Python3 was released in 2008:.

• If the user inputs TRUE, print out Correct.

• If the user inputs FALSE, print out Incorrect.

• Any other user input should result in Please answer TRUE or FALSE.

Go to your main.py file and add your code to it. Then, run it in a terminal. The output should look like Snippet 3.12:

python3 main.py
Return TRUE or FALSE: Python3 was released in 2008:
TRUE
Correct
Have a great day!
python3 main.py
Return TRUE or FALSE: Python3 was released in 2008:
FALSE
Incorrect
Have a great day!


python3_year = 2008
year = int(input('When was Python3 first released?'))

if year == python3_year:
	print('That is correct.')
elif year > python3_year:
	print('Incorrect, too late.')
elif year < python3_year:
    print('Incorrect, too early.')
print('Have a great day!')

'''
python3_year = 2008
year = input('Return TRUE or FALSE: Python3 was released in 2008: ')

if year == "TRUE":
    print("Correct")
elif year == "FALSE":
    print("Incorrect")
else:
    print("Please answer TRUE or FALSE")

print("Have a great day!")
