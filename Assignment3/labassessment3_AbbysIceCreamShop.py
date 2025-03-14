'''
Scenario
Abby has always dreamed of having her own ice cream shop. Now as a young entrepreneur she has decided to pursue her dream, but she needs some help in determining the financial viability of her plan. She has come up with a list of income and expense parameters and needs a simple program to input these parameters and calculate the monthly profit or loss as well as performing some variable cost what-if analysis.

For expenses, she has:

Raw ingredient cost per serving
Hourly labor rate
Real estate monthly rental
Utilities per month
Monthly advertising budget
On the income side, she has:

Selling price per serving (assume only one size for simplicity)
Number of servings sold per month
Based on some research, she has determined that a single employee can run the shop and she plans to have the shop open eight hours per day and six days per week.

Best Practices to Follow:
Write detailed comments and doc-strings.
Use logical variable names with a consistent convention.
Organize and structure your code for readability.
Use hand calculations to verify the formulas in your code. I.e. write your own test cases to check correctness.
Create the text-based, menu interface
Write a Python script with a menu driven, text-based user interface that looks like this:

Expenses:
1. Cost per serving: 1.0
2. Labor rate per hour: 7.5
3. Shop rental per month: 800
4. Utilities per month: 150
5. Advertising budget per month: 100

Income:
6. Selling price (each): 4.0
7. Servings sold per month: 500

Analysis:


Enter Selection (0 to Exit):
In which the current parameter value is displayed but the user can select and modify each one. For Example:

Enter Selection (0 to Exit): 1
Enter cost per serving:
Use the following as the default starting values:

serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 1000
selling_price = 4.00

Add Profit/Loss functionality
At this point, your script should allow the user to input values for all the variables needed to calculate the profit (or loss) of Abby’s Ice Cream business. To add this functionality, start by adding the menu item

8. Profit/Loss Calculation
under the Analysis section of the menu. If the user selects option 8, the script should display something like the following:

Enter Selection (0 to Exit): 8
The Ice Cream Shop will have a monthly profit/loss of 90.0 or 0.18 per serving.
In order to perform these calculations, you’ll have to think back to Algebra and calculate things like the total expenses and the total income on a monthly basis. Finally, in order to keep the values in monetary precision, you can use the round() function with a precision of 2.



Task #04: Add profit/loss calculations.



Add "What if" analysis
Add the following item to your menu:

9. "What If" analysis with 10% variance
If the user selects option 9, the script should vary the expenses followed by the income from negative to positive ten percent by increments of 2. This will help Abby with some “what-if” calculations:

Enter Selection (0 to Exit): 9

Varying the Expenses From -10% to +10%::
Percent:  -10 Expenses:  3141.0 Profit/Loss:  859.0
Percent:  -8 Expenses:  3210.8 Profit/Loss:  789.2
Percent:  -6 Expenses:  3280.6 Profit/Loss:  719.4
Percent:  -4 Expenses:  3350.4 Profit/Loss:  649.6
Percent:  -2 Expenses:  3420.2 Profit/Loss:  579.8
Percent:  0 Expenses:  3490.0 Profit/Loss:  510.0
Percent:  2 Expenses:  3559.8 Profit/Loss:  440.2
Percent:  4 Expenses:  3629.6 Profit/Loss:  370.4
Percent:  6 Expenses:  3699.4 Profit/Loss:  300.6
Percent:  8 Expenses:  3769.2 Profit/Loss:  230.8

Varying the Income From -10% to +10%::
Percent:  -10 Income:  3600.0 Profit/Loss:  110.0
Percent:  -8 Income:  3680.0 Profit/Loss:  190.0
Percent:  -6 Income:  3760.0 Profit/Loss:  270.0
Percent:  -4 Income:  3840.0 Profit/Loss:  350.0
Percent:  -2 Income:  3920.0 Profit/Loss:  430.0
Percent:  0 Income:  4000.0 Profit/Loss:  510.0
Percent:  2 Income:  4080.0 Profit/Loss:  590.0
Percent:  4 Income:  4160.0 Profit/Loss:  670.0
Percent:  6 Income:  4240.0 Profit/Loss:  750.0
Percent:  8 Income:  4320.0 Profit/Loss:  830.0
In all these calculations, assume that the shop operates with a single employee for eight hours per day, six days a week, for four weeks.

-----------------------------------------------------------------
Abby has always dreamed of having her own ice cream shop. Now as a young entrepreneur she has decided to pursue her dream, but she needs some help in determining the financial viability of her plan. She has come up with a list of income and expense parameters and needs a simple program to input these parameters and calculate the monthly profit or loss as well as performing some variable cost what-if analysis.

For expenses, she has:
Raw ingredient cost per serving
Hourly labor rate
Real estate monthly rental
Utilities per month
Monthly advertising budget
On the income side, she has:

Selling price per serving (assume only one size for simplicity)
Number of servings sold per month
Based on some research, she has determined that a single employee can run the shop and she plans to have the shop open eight hours per day and six days per week.


Use logical variable names with a consistent convention.
Use hand calculations to verify the formulas in your code. I.e. write your own test cases to check correctness.
Create the text-based, menu interface
Write a Python script with a menu driven, text-based user interface that looks like this:

Expenses:
1. Cost per serving: 1.0
2. Labor rate per hour: 7.5
3. Shop rental per month: 800
4. Utilities per month: 150
5. Advertising budget per month: 100

Income:
6. Selling price (each): 4.0
7. Servings sold per month: 500

Analysis:


Enter Selection (0 to Exit):
In which the current parameter value is displayed but the user can select and modify each one. For Example:

Enter Selection (0 to Exit): 1
Enter cost per serving:
Use the following as the default starting values:

serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 1000
selling_price = 4.00
'''

serving_cost = 1.00
labor_rate = 7.50            
shop_rental = 800            
utilities = 150             
advertising = 100           
selling_price = 4.00         
servings_per_month = 1000   

labor_hours = 8 * 6 * 4  # 192 hours

menu = True

while menu:

    print("Expenses:")
    print(" 1. Cost per serving: 1.0")
    print(" 2. Labor rate per hour: 7.5")
    print(" 3. Shop rental per month: 800")
    print(" 4. Utilities per month: 150")
    print(" 5. Advertising budget per month: 100\n")
    
    print("Income:")
    print(" 6. Selling price (each): 4.0")
    print(" 7. Servings sold per month: 1000\n")
    
    print("Analysis:")
    print(" 8. Profit/Loss Calculation")
    print(' 9. "What If" analysis with 10% variance')
    print(" 0 to Exit")
    
    print("\nEnter Selection (0 to Exit): ")
    menuNav = int(input())
    
    if menuNav == 1:
        serving_cost = float(input("Enter new cost per serving: "))
    elif menuNav == 2:
        labor_rate = float(input("Enter new labor rate per hour: "))
    elif menuNav == 3:
        shop_rental = float(input("Enter new shop rental cost: "))
    elif menuNav == 4:
        utilities = float(input("Enter new utilities cost: "))
    elif menuNav == 5:
        advertising = float(input("Enter new advertising cost: "))
    elif menuNav == 6:
        selling_price = float(input("Enter new selling price (each): "))
    elif menuNav == 7:
        servings_per_month = int(input("Change Servings Per Month: "))
    elif menuNav == 8:
        total_income = selling_price * servings_per_month
        total_expenses = (serving_cost * servings_per_month) + (labor_rate * labor_hours) + shop_rental + utilities + advertising
        profit_loss = total_income - total_expenses
        profit_per_serving = profit_loss / servings_per_month if servings_per_month != 0 else 0

        profit_loss = round(profit_loss, 2)
        profit_per_serving = round(profit_per_serving, 2)
        
        print(f"\nThe Ice Cream Shop will have a monthly profit/loss of {profit_loss} or {profit_per_serving} per serving.\n")
    elif menuNav == 9:
        base_income = selling_price * servings_per_month
        base_expenses = (serving_cost * servings_per_month) + (labor_rate * labor_hours) + shop_rental + utilities + advertising
        
        print("\nVarying the Expenses From -10% to +10%::")
        for p in range(-10, 10, 2):
            new_expenses = base_expenses * (1 + p/100)
            new_profit = base_income - new_expenses

            new_expenses = round(new_expenses, 1)
            new_profit = round(new_profit, 1)
            print(f"Percent: {p:3d} Expenses: {new_expenses} Profit/Loss: {new_profit}")
        
        print("\nVarying the Income From -10% to +10%::")
        for p in range(-10, 10, 2):
            new_income = base_income * (1 + p/100)
            new_profit = new_income - base_expenses
            new_income = round(new_income, 1)
            new_profit = round(new_profit, 1)
            print(f"Percent: {p:3d} Income: {new_income} Profit/Loss: {new_profit}")
            
        print("")
    elif menuNav == 0:
        menu = False
    else:
        print("Invalid selection. Please choose again.\n")

print(f"\nUpdated Serving Cost: {serving_cost}")
print(f"Updated Labor Rate: {labor_rate}")
print(f"Updated Shop Rental Cost: {shop_rental}")
print(f"Updated Utilities Cost: {utilities}")
print(f"Updated Advertising Cost: {advertising}")
print(f"Updated Selling Price: {selling_price}")
print(f"Updated Servings Per Month: {servings_per_month}")