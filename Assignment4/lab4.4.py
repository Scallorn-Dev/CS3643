'''
Scenario
You need a quick way to work out exponential values given one base number and a second number.

Aim
Write a lambda function that takes in two numerical values and returns the first value, raised to the power of the second value:

Steps for Completion
Create a lambda function that takes in number and power and returns the value of the number raised to power.

Assign it to a variable called exponential.

Print the exponential variable.

Using the numberical values 2 and 6, the output should be as shown in Snippet 4.42:

64
Snippet 4.42



Task #01: Implement the lambda function and assign the return value to the variable exponential.
'''

exponential = lambda number, power: number ** power
print(exponential(2,6))