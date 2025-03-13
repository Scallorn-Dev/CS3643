'''
Scenario
You have been given three code snippets that need to be completed in order to execute.

Aim
In each of the code snippets replace the ? character with the correct Boolean operator, for instance <,>,==,not, or not in. Each code block should execute correctly.

After you have executed a code snippet, run the corresponding task to ensure you have passed before moving on to the next snippet.

Steps for Completion
Consider the following code in Snippet 2.82:
num = 61
if num % 2 ? 0:
	print("Odd")
Snippet 2.82

Consider the following code in Snippet 2.83:
days = 32
if days ? 31:
	print("Not a valid day of the month.")
Snippet 2.83

Consider the following code in Snippet 2.84:
character = "c"
if character ? ["a", "i"]:
    print(f"The letter '{character}' does not also constitute a word.")
Snippet 2.84
'''

num = 61
if num % 2 != 0:
    print("Odd")

days = 32
if days > 31:
    print("Not a valid day of the month.")

character = "c"
if character not in ["a", "i"]:
    print(f"The letter '{character}' does not also constitute a word.")
