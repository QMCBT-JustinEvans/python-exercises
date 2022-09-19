"""1. Conditional Basics"""

"""a. prompt the user for a day of the week, print out whether the day is Monday or not
"""
day_of_the_week = input('Day of the Week: ')
if day_of_the_week == 'Monday' or day_of_the_week == 'monday':
    print("It's another wonderful Monday!")
else:
    print(f'{day_of_the_week} is just another day of the week.')

"""b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
"""
weekday = ['Monday', 'Mon', 'monday', 'mon', 'Tuesday', 'Tues', 'tuesday', 'tues', 'Wednesday', 'Wed', 'wednesday', 'wed', 'Thursday', 'Thur', 'thursday', 'thur', 'Friday', 'Fri', 'friday', 'fri']
weekend = ['Saterday', 'Sat', 'saterday', 'sat', 'Sunday', 'Sun', 'sunday', 'sun']
day_of_the_week = input('Day of the Week: ')
if day_of_the_week in weekday:
    print(f'{day_of_the_week} is a weekday.')
elif day_of_the_week in weekend:
    print(f'{day_of_the_week} is on the weekend.')
else:
    print(f'{day_of_the_week} is not a valid day of the week!')

"""c. create variables and make up values for

* the number of hours worked in one week
* the hourly rate
* how much the week's paycheck will be

write the python code that calculates the weekly paycheck. 
You get paid time and a half if you work more than 40 hours.
"""
weekly_hours_worked = 40
hourly_wage = 10
weekly_paycheck = weekly_hours_worked * hourly_wage
overtime = hourly_wage * 1.5

if weekly_hours_worked <= 40: 
    print(weekly_paycheck)

elif weekly_hours_worked > 40: 
    print(weekly_hours_worked * overtime)

"""2. Loop Basics"""

"""a. While"""

"""
* Create an integer variable i with a value of 5.
* Create a while loop that runs so long as i is less than or equal to 15
* Each loop iteration, output the current value of i, then increment i by one.

Your output should look like this:

5
6
7
8
9
10
11
12
13
14
15
"""
i = int(5)
while i <= 15:
    print(i) # order of print matters
    i += 1

"""
* Create a while loop that will count by 2's starting with 0 and ending at 100. 
Follow each number with a new line.
"""
i = 0
while i <= 100:
    print(i)
    i += 2

"""
* Alter your loop to count backwards by 5's from 100 to -10.
"""
i = 100
while i >= -10 and i <= 100: # order is important!
    # less than 100 listed first will NOT stop at -10
    print(i)
    i -= 5

"""
* Create a while loop that starts at 2, 
and displays the number squared on each line while the number is less than 1,000,000. 

Output should equal:

 2
 4
 16
 256
 65536
"""
number = 2
while number < 1000000:
    print(number)
    number **= 2

"""
Write a loop that uses print to create the output shown below.

100
95
90
85
80
75
70
65
60
55
50
45
40
35
30
25
20
15
10
5
"""
i = 100
while i >= 5 and i <= 100:
    print(i)
    i -= 5

"""
b. For Loops
"""

"""
i. Write some code that prompts the user for a number,
then shows a multiplication table up through 10 for that number.

For example, if the user enters 7, your program should output:

7 x 1 = 7 
7 x 2 = 14 
7 x 3 = 21 
7 x 4 = 28 
7 x 5 = 35 
7 x 6 = 42 
7 x 7 = 49 
7 x 8 = 56 
7 x 9 = 63 
7 x 10 = 70
"""
multipliers = map(int, list(range(1,11)))
number = int(input('Choose a whole number: '))
for multiplier in multipliers:
    result = number * multiplier
    print(f'{number} x {multiplier} = {result}')

"""
ii. Create a for loop that uses print to create the output shown below.

1
22
333
4444
55555
666666
7777777
88888888
999999999
"""
a = 1 # a not needed i * i would work
for i in range(1,10):
    print(str(a)*i)
    a += 1