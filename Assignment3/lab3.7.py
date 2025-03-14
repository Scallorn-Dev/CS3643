'''
Aim
Using a for loop and a range function, you have been asked to find the even numbers between 5 and 55 and then find their sum.

Steps for Completion
Define a counter for the sum named total_sum.

Define a for loop with an even range for numbers between 5 and 55.

Add each looped number to the sum.

Outside the loop, print out total_sum.

The output should be as shown in Snippet 3.50:

750
'''
total_sum = 0 

for x in range(5, 56):  # Start at 5, go up to 55
    if x % 2 == 0:  # checking if the number is positive
        total_sum += x 

print(total_sum)  
