'''
Scenario
You work for a small company that exports artisan chocolate. Although you measure your products in kilograms, you often get orders in both pounds and ounces. You have decided that rather than have to look up conversions all the time, you could use Python code to take inputs to make conversions between the different units of measurement.

You will write three blocks of code. The first will convert kilograms to pounds and ounces. The second will convert pounds to kilograms and ounces. The third will convert ounces to kilograms and pounds.

The conversions are as follows:

1 kilogram = 35.274 ounces
1 kilogram = 2.20462 pounds
1 pound = 0.453592 kilograms
1 pound = 16 ounces
1 ounce = 0.0283 kilograms
1 ounce = 0.0625 pounds
For the purposes of this activity the template for a function has been provided. You have not yet covered functions in the course, but they are a way of reusing code. Like a Python script, a function can have zero or more parameters. In the code window you will see three functions defined as def convert_kg(value):, def convert_pounds(value):, and def convert_ounces(value):. Each function will have a block showing you where to place your code.

Best Practices to Follow:
Within the functions you will see a line telling you where to write the code.

Writing detailed comments and docstrings.
Organizing and structuring code for readability.
It is recommended that you use your own test cases in order to check for correctness. You can test your code inside the __main__ provided.
'''

def convert_kg(value):
    initialKG = value
    kgToPounds = initialKG * 2.20462
    kgToOunces = initialKG * 35.274

    return kgToPounds, kgToOunces


def convert_pounds(value):
    initialPound = value
    poundsToKg = initialPound * 0.453952
    poundsToOunces = initialPound * 16
    
    return poundsToKg, poundsToOunces


def convert_ounces(value):
    initialOunce = value
    ouncesToKg = initialOunce * 0.0283
    ouncesToPounds = initialOunce * 0.0625
    
    return ouncesToKg, ouncesToPounds


if __name__ == "__main__":
    initialAmount = 10

    kg_to_pounds, kg_to_ounces = convert_kg(initialAmount)
    pounds_to_kg, pounds_to_ounces = convert_pounds(initialAmount)
    ounces_to_kg, ounces_to_pounds = convert_ounces(initialAmount)

    print("The value after conversion for KG to pounds is:", kg_to_pounds, "and KG to ounces is:", kg_to_ounces)
    print("The value after conversion for Pounds to kg's is:", pounds_to_kg, "and Pounds to ounces is:", pounds_to_ounces)
    print("The value after conversion for Ounces to kg's is:", ounces_to_kg, "and Ounces to pounds is:", ounces_to_pounds)
