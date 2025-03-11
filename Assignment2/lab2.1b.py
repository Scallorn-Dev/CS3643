'''
Scenario
You are given the number of days that you have been driving, and you will write a Python script to work out the equivalent number of years and weeks.

Aim
Write a script that takes user input as days and converts the days into years, weeks, and days, and then prints them out. We can ignore leap years. The aim of this activity is to use different arithmetic operators to split days into years, weeks, and days.

Steps for Completion
Go to your main.py file.

On the first line, ask the user how many days they've been driving for and declare the user input. It's an integer, so cast the string.

Then calculate the number of years in that set of days.

Next, convert the remaining days that weren't converted to years into weeks.

Then, get any remaining days that weren't converted to weeks.

Print everything out.

Finally, run the script with the python3 main.py command.

The output should look like Figure 2.5 shown below:
workspace $ python3 main.py
Days you have been driving: 1000
You have been driving for:
years: 2
weeks: 38
days: 4
'''
num = int(input("How many days have you been driving for?: "))  # Taking input as an integer

oneYear = 365
oneWeek = 7

yearsDriving = num // oneYear # // interger division

remainingDays = num % oneYear #mod year to get remainder

weeksDriving = remainingDays // oneWeek

daysDriving = remainingDays % oneWeek #getting the remaining days that werent converted to weeks

print(f"Days you have been driving: {num}")
print("You have been driving for:")
print(f"Years: {yearsDriving}")
print(f"Weeks: {weeksDriving}")
print(f"Days: {daysDriving}")
