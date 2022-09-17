""" Identify the data type of the following values:"""

type(99.9) #float
type("False") #str
type(False) #bool
type('0') #str
type(0) #int
type('True') #str
type(True) #bool
type([{}]) #List of a dictionary
type({'a': []}) #dict with "a" as a list

"""What data type would best represent:"""

"""A term or phrase typed into a search box?"""
#str
"""If a user is logged in?""" 
#bool
"""A discount amount to apply to a user's shopping cart?"""
#int (float would cover int and % off)
"""Whether or not a coupon code is valid?"""
#bool
"""An email address typed into a registration form?"""
#str
"""The price of a product?"""
#float
"""A Matrix?"""
#NoneType (list of list)
"""The email addresses collected from a registration form?"""
#list
"""Information about applicants to Codeup's data science program?"""
#dictionary

"""For each of the following code blocks, 
read the expression and predict what the result of evaluating it would be, 
then execute the expression in your Python REPL."""

'1' + 2 #equals 3 because python assumes 1 as an int (I was wrong; error)
6 % 4 #returns the remainder of 6 divided by 4
type(6 % 4) #float because python prepares for a return of float when dividing 
            #(I was wrong; int, because it is the type of the return)
type(type(6 % 4)) #this will return 'type' because the return of type(6 % 4) results in the type(int)
'3 + 4 is ' + 3 + 4 #error because you cannot sum a str with an int
0 < 0 #False
'False' == False #False because str != bool
True == 'True' #also False because bool != str
5 >= -5 #True
True or "42" #True because True is True else("42")
6 % 5 #remainder 1
5 < 4 and 1 == 1 #False because both AND statements are not True
'codeup' == 'codeup' and 'codeup' == 'Codeup' #False because both AND statements are not True 'c' vs 'C'
4 >= 0 and 1 !== '1' #True because both AND statements are True
                    #I was wrong... I thought dbl = looked out of place with ! for NOT =
"""Also, you would need to fully state the second AND query""" 
4 >= 0 and 4 != '1'
4 >= 0 and != '1'
4 >= 0 and 1 != '1' # I originally missed the first 1 in the query
6 % 3 == 0 #True
5 % 2 != 0 #True
[1] + 2 #error cannot sum list with int
[1] + [2] #[1, 2] returns concat of lists (I initially wrote this as [1, 2] but changed it)
[1] * 2 #I thought this would multiply the items of the list by 2
        #but it actually multiplied the list by 2 creating a larger list
        #I tried it *3 and with a larger list to test functionality
[1] * [2] #error, cannot multiply by non int 
[] + [] == [] #False because empty or 0 equals False (I was wrong)
{} + {} #error, you cannot concat libraries (dictionary)

"""Create a Python script file named data_types_and_variables.py. 
Inside it, write some Python code, that is, variables and operators, 
to describe the following scenarios. 
Do not worry about the real operations to get the values, 
the goal of these exercises is to understand how real world conditions 
can be represented with code.
"""

"""You have rented some movies for your kids: 
The little mermaid (for 3 days), 
Brother Bear (for 5 days, they love it), 
and Hercules (1 day, you don't know yet if they're going to like it). 
If price for a movie per day is 3 dollars, 
how much will you have to pay?
"""
number_of_movies_rented = 3
#I could have simply added in my head for total_days_rented but wanted to show my work
little_mermaid_days_rented = 3
brother_bear_days_rented = 5
hercules_days_rented = 1
total_days_rented = little_mermaid_days_rented + brother_bear_days_rented + hercules_days_rented
rental_price_per_day = 3
I_will_have_to_pay = total_days_rented * rental_price_per_day
I_will_have_to_pay

"""Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
they pay you a different rate per hour. 
Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
How much will you receive in payment for this week? 
You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
"""
google_pay = 400
google_work = 6
amazon_pay = 380
amazon_work = 4
facebook_pay = 350
facebook_work = 10
weekly_pay = google_pay * google_work + amazon_pay * amazon_work + facebook_pay * facebook_work
weekly_pay

"""A student can be enrolled to a class only if the class is not full 
and the class schedule does not conflict with her current schedule.
"""
class_full = False
schedules_conflict = False
if class_full == False and schedules_conflict == False: print('can_enroll')
else: print('can_not_enroll')

"""A product offer can be applied only if people buys more than 2 items, 
and the offer has not expired. 
Premium members do not need to buy a specific amount of products.
"""

items_bought = 2
offer_expires = 20221031
premium_member = False

if offer_expires < 20220916: offer_expired = True
else: offer_expired = False

if items_bought > 2 or premium_member == True: required_items_bought = True 
else: required_items_bought = False

if required_items_bought == True and offer_expired == False: print('Product Offer Valid') 
else: print('Product Offer NOT Valid')

"""Continue working in your data_types_and_variables.py file. 
Use the following code to follow the instructions below:
"""
username = 'codeup'
password = 'notastrongpassword'

"""Create a variable that holds a boolean value for each of the following conditions:"""

"""the password must be at least 5 characters"""
len(password) >= 5 

"""the username must be no more than 20 characters"""
len(username) > 20 

"""the password must not be the same as the username"""
username == password

"""bonus neither the username or password can start or end with whitespace"""
