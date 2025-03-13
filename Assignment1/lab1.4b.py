'''
Aim
Write a script that takes a whole number from a user’s input and prints out its 2's multiplication table till 10.

Steps for Completion
Go to your main.py file.

On the first line, add a docstring explaining what your file does. Then, assign a variable called whole_num to the user’s input and cast it to an integer.

Next, print 10 underscores as the top border of the table.

On the first line print your whole number, then multiply your whole number by multiples of 2's till 10 and print that out.

Finally, print 10 underscores again for the bottom border of the table, as in step 3.

Run the file by using the python3 main.py command.

Generate a multiplication table for: 7
___________
Number: 7
2: 14
4: 28
6: 42
8: 56
10: 70

'''
whole_num = int(input("Generate a multiplication table for: "))

print("__________")
print(f"1: {whole_num}")

for i in range(2, 11, 2): # starting at 2 up to 10 stepping by 2's 
    print(f"{i}: {whole_num * i}")

print("__________")
