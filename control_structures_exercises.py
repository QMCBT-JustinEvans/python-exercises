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

"""
c. break and continue
"""

"""
i. Write a program that prompts the user for a positive integer. 
Next write a loop that prints out the numbers from the number the user entered down to 1.
"""
pos_int = int(input('Choose a Posititive Intiger: '))
while pos_int > 0:
    print(pos_int)
    pos_int -= 1
    if pos_int == 0:
        break
    else:
        print(f'{pos_int} is not a positive integer!')  

"""
ii. The input function can be used to prompt for input 
and use that input in your python code. 

Prompt the user to enter a positive number 
and write a loop that counts from 0 to that number. 

(Hints: first make sure that the value the user entered is a valid number, 
also note that the input function returns a string, 
so you'll need to convert this to a numeric type.)
"""
pos_int = int(input('Choose a Posititive Intiger: '))
number = 0
while pos_int > 0:
    print(number)
    number += 1
    if number > pos_int:
        break
    else:
        print(f'{pos_int} is not a positive integer!')    

"""
iii. Prompt the user for an odd number between 1 and 50. 
Use a loop and a break statement to continue prompting the user if they enter invalid input. 
(Hint: use the isdigit method on strings to determine this). 
Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
except for the number the user entered.

Your output should look like this:
Number to skip is: 27

Here is an odd number: 1
Here is an odd number: 3
Here is an odd number: 5
Here is an odd number: 7
Here is an odd number: 9
Here is an odd number: 11
Here is an odd number: 13
Here is an odd number: 15
Here is an odd number: 17
Here is an odd number: 19
Here is an odd number: 21
Here is an odd number: 23
Here is an odd number: 25
Yikes! Skipping number: 27
Here is an odd number: 29
Here is an odd number: 31
Here is an odd number: 33
Here is an odd number: 35
Here is an odd number: 37
Here is an odd number: 39
Here is an odd number: 41
Here is an odd number: 43
Here is an odd number: 45
Here is an odd number: 47
Here is an odd number: 49
"""
while True:
    odd_num = input('Enter an odd number between 1 and 50: ')
    
    if odd_num.isdigit():
        #print('This is a digit')
        if int(odd_num) % 2 != 0:
            #print('This is an odd number')
            if (int(odd_num) > 1) and (int(odd_num) < 50):
                #print('This number is between 1-50')
                break
                
odd_num = int(odd_num)            
                
for i in range(1, 50):
    if i == odd_num:
        print(f'Yikes! Skipping number: {odd_num}')
        continue
    if i % 2 == 1:
        print(f'Here is an odd number: {i}')

"""
3. Fizzbuzz
"""

"""
One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
Developed by Imran Ghory, the test is designed to test basic looping 
and conditional logic skills.

* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number
* For the multiples of five print "Buzz".
* For numbers which are multiples of both three and five print "FizzBuzz".
"""
for i in range(1,101):
    if i % 15 == 0:
        print(f'{i} - FizzBuzz')
        continue
    if i % 3 == 0:
        print (f'{i} - Fizz')
        continue
    if i % 5 == 0:
        print(f'{i} - Buzz')
        continue
    print(i)

"""
4. Display a table of powers.
"""

"""
* Prompt the user to enter an integer.
* Display a table of squares and cubes from 1 to the value entered.
* Ask if the user wants to continue.
* Assume that the user will enter valid data.
* Only continue if the user agrees to.

Example Output
What number would you like to go up to? 5

Here is your table!

number | squared | cubed
------ | ------- | -----
1      | 1       | 1
2      | 4       | 8
3      | 9       | 27
4      | 16      | 64
5      | 25      | 125
"""
while True:
    user_num = int(input('Choose an integer: '))

    for i in range(1, user_num + 1):
        print(f'{i} |{i**2} |{i**3}')
    
    user_yn = input('Would you like to continue? y/n: ')
    if user_yn.lower() != 'y':
        break

"""
Bonus: Research python's format string specifiers to align the table
"""

"""
5. Convert given number grades into letter grades.

* Prompt the user for a numerical grade from 0 to 100.
* Display the corresponding letter grade.
* Prompt the user to continue.
* Assume that the user will enter valid integers for the grades.
* The application should only continue if the user agrees to.
* Grade Ranges:

    * A : 100 - 88
    * B : 87 - 80
    * C : 79 - 67
    * D : 66 - 60
    * F : 59 - 0
"""
while True:
    user_grade = int(input('Enter a numerical grade 1-100: '))
    if user_grade >=88:
        print('A')
    elif user_grade >=80:
        print('B')
    elif user_grade >=67:
        print('C')
    elif user_grade >=60:
        print('D')
    else:
        print('F')
    
    user_yn = input('Would you like to continue? y/n: ')
    if user_yn.lower() != 'y':
        break

"""
Bonus
Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
"""

"""
6. Create a list of dictionaries where each dictionary represents a book that you have read. 
Each dictionary in the list should have the keys title, author, and genre. 
Loop through the list and print out information about each book.
"""


"""
a. Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
"""
