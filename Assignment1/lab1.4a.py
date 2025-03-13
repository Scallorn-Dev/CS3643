'''
Scenario
You have been given some Python code that doesn't work due to syntax errors and you need to fix the code by correcting poor indentations.

Aim
To fix the code snippet in the main.py file from the code bundle to have the appropriate indentation in each block. After you fix it, run the script in the terminal and verify that you get the output. Don't worry if you don't understand what the code is doing; the goal is to get comfortable with indentations. The incorrect code is also shown in Snippet 1.71 below:

if 14 > 7:
    print("Greater than")
   x = 2
  print(x * 7)
else:
    print("Less than")
   print(7)
Snippet 1.71

Hint: Indentation for statements in a block is dictated by the first statement's indentation level.

The output of the correct syntax should be as shown in Snippet 1.72:

Greater than
14
'''

if 14 > 7:
    print("Greater than")
    x = 2
    print(x * 7)
else:
    print("Less than")
    print(7)


