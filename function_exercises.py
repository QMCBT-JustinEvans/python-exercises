#!/usr/bin/env python
# coding: utf-8

# #### Function Exercises
# 
# Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[1]:


def is_two(n):
    return n == 2 or n == '2'
    
print(is_two(2))
print(is_two("2"))
print(is_two(3))


# Notes for my own testing curiosity:

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[2]:


def is_vowel(vowel):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if vowel in vowels:
        return True
    else:
        False
    
print(is_vowel('A'))
print(is_vowel('a'))
print(is_vowel('b'))
print(is_vowel('B'))


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[7]:


def is_consonant(non_vowel):
    if not is_vowel(non_vowel):
        return True
    else:
        return False
    
print(is_consonant('a'))
print(is_consonant('A'))
print(is_consonant('b'))


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[20]:


def is_word(somestring):
    if type(somestring) == str:
        if is_consonant(somestring[0]):
            return somestring.capitalize()
        else:
            False
    else:
        False

print(is_word('baby'))
print(is_word('apple'))


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[35]:


def calculate_tip(tip_percent, bill_total):
    #tip_percent = float(input('Enter decimal percent between 0-1 (example 20% = 0.20): '))
    #bill_total = float(input('Bill Total: '))
    tip = bill_total * tip_percent
    grand_total = bill_total + tip
    return print(f'${bill_total} Bill Total + {int(tip_percent*100)}% Tip = ${round(tip,2)} for a Grand Total of ${round(grand_total,2)}')

calculate_tip(.20, 37.48)


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[28]:


def apply_discount():
    original_price = float(input('Original Price: '))
    discount_percentage = float(input('Enter discount percent as decimal between 0-1 (example 10% = 0.10): '))
    price = round(original_price-(original_price*discount_percentage),2)
    return print(f'Price is ${price}')

apply_discount()


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[29]:


def handle_commas(somestring):
    if type(somestring) == str:
        return int(somestring.replace(',', ''))
    else:
        return somestring
    
print(handle_commas('1,000,000,000'))


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[31]:


def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

print(get_letter_grade(52))
print(get_letter_grade(62))
print(get_letter_grade(72))
print(get_letter_grade(82))
print(get_letter_grade(92))


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[32]:


def remove_vowels(word):
    new_word = ''
    for i in word:
        if not is_vowel(i):
            new_word += i
    return new_word

print(remove_vowels("sequoia"))


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# * anything that is not a valid python identifier should be removed
# * leading and trailing whitespace should be removed
# * everything should be lowercase
# * spaces should be replaced with underscores
# * for example:
# 
#     * Name will become name
#     * First Name will become first_name
#     * % Completed will become completed

# In[33]:


def normalize_name(somestring):
    newstring = ''
    #grab all letter, number, spaces
    for letter in somestring:
        if letter.isidentifier() or letter == ' ':
            newstring += letter
    # loops to check if leading char is letter
    for letter in newstring:
        if letter.isalpha():
            break
        else:
            newstring = newstring[1:]
    return newstring.strip().lower().replace(' ', '_')

print(normalize_name('Name'))
print(normalize_name('First Name'))
print(normalize_name('% Completed'))


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
# * cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# * cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[34]:


def cumulative_sum(list):
    newlist = []
    for n in range (1, len(list)+1):
        cumsum = sum(list[:n])
        newlist.append(cumsum)
    return newlist

print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([1, 2, 3, 4]))
print(cumulative_sum([4, 5, 6, 7]))
print(cumulative_sum([7, 8, 9, 10]))


# ### Additional Exercise
# 
# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 
# in order to thouroughly comment your code to explain your code.

# In[ ]:





# ## Bonus
# 
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[ ]:





# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# 
# * col_index('A') returns 1
# * col_index('B') returns 2
# * col_index('AA') returns 27

# In[ ]:




