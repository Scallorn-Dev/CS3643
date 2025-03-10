'''
sing variables write a script that defines a distance of 60 miles and a completion time of 3 hours. The output should show a completion speed in miles per hour, knots, and feet per second.

Here are some hints:

The formula for calculating speed is distance/time = speed.
To convert miles to knots, divide the miles by 1.15078.
To convert miles to feet, multiply the miles by 5280.
To convert hours to seconds, multiply hours by 3600.

Go to your main.py file.

On the first two lines, declare two variables for the distance in miles and time in hours and assign the values 60 and 3, respectively.

In the next two lines, calculate the distance in knots and distance in feet based on the distance in miles.

Then, calculate the time in seconds based on the time in hours.

Next, calculate the speed in knots, speed in miles per hour, and speed in feet per second.

Finally, add print statements to print out the results.

In your terminal, run the script by using the python3 main.py command.
'''

miles = 60
time = 3

speed = miles/time

knots = speed / 1.15078

feet = miles * 5280

seconds = time * 3600

feetps = feet/seconds

print("feet: ", feet)
print("seconds: ", seconds)


print ("The speed in knots is: ", knots)
print ("The speed in miles per hour is: ", speed)
print ("The speed in feet per second is: ", feetps)