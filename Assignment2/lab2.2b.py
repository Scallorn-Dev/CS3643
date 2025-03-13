'''
Scenario
You want to write a Python script that takes a string and counts the occurrence of a specified word.

Aim
Write a script that counts and displays the number of occurrences of a specified word in a given excerpt. The script should request two input values from the user, that is, the excerpt and the word to search for. You can assume that the word will not occur as a substring in other words.

Steps for Completion
Go to your main.py file.

Take in the user input for the sentence and the substring.

Next, sanitize and format the input by removing the whitespace and converting it to lowercase.

Count the occurrences of the substring.

Print the results.

Run the script by using the python3 main.py command

'''

userStr = input("Sentence: ").strip().lower()
subStr = input("Word to look for in sentence: ").strip().lower()


words = userStr.split() #Splitting the sentence into words


count = words.count(subStr) #counting the number of instance of subStr


print(f"There are {count} occurrences of '{subStr}' in the sentence.")