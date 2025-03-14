'''
Scenario
You have been asked to write a loop that outputs values in a database column ranging between 10 and 100. Any number that is not divisible by 5, and any value that is not an integer, should be ignored. When the value in the loop hits 95, break the loop prematurely. One of your team members has advised the use of break, continue, and pass statements.

Steps for Completion
Define a for loop, using the range function to create the lower (10) and upper (100) limits.

Define a condition that checks for zero.

Define a condition that checks whether the number is divisible by 5.

Define a condition that checks the data type.

Define a condition that checks for 95, and breaks the loop.

Define a condition that uses the pass statement if the number doesn't meet any condition.

Print the number if it meets the condition.

The output will be as shown in Snippet 3.65:

10
15
20
25
30
35
...
...
80
85
90
'''

for number in range(10, 100):
    if number % 5 != 0: #checking if the number is divisible by 5
        continue  
    
    elif not isinstance(number, int): #checking if the number is an int
        pass 
    
    else:
        print(number)
    
    if number == 95:
        break
