#!/usr/bin/env python
# coding: utf-8

# #### Function Exercises
# 
# Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[126]:


n = input('Choose a number: ')
def is_two(n):
    return n == 2 or n == '2'


# In[132]:


is_two(n)


# Notes for my own testing curiosity:

# In[125]:


print(f'is_two(n) is int        -', is_two(n) == 2),
print(f'is_two(n) is str        -', is_two(n) == '2'),
print(f'is_two(n) is forced int -', int(is_two(n)) == 2)
print(f'is_two(n) is            -', is_two(n))
print()
print(f'{n} is int        -', n == 2),
print(f'{n} is str        -', n == '2'),
print(f'{n} is forced int -', int(n) == 2)
print(f'{n} is            -', n)


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[143]:


v = input('Choose a vowel: ').lower()
vowels = ('a', 'e', 'i', 'o', 'u')
def is_vowel(v):
    if v in vowels:
        return True


# In[144]:


is_vowel(v)


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[153]:


vowels = ('a', 'e', 'i', 'o', 'u')

def is_consonant(non_vowel):
    if non_vowel not in vowels:
        return True


# In[151]:


print(is_consonant('j'))
print(is_consonant('a'))


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[154]:


def is_word(word):
    


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[186]:


tip_percent = float(input('Enter decimal percent between 0-1 (example 20% = 0.20): '))
bill_total = float(input('Bill Total: '))
tip = bill_total * tip_percent
grand_total = bill_total + tip

def calculate_tip(grand_total):
    return print(f'${bill_total} Bill Total + {int(tip_percent*100)}% Tip = ${round(tip,2)} for a Grand Total of ${round(grand_total,2)}')


# In[187]:


calculate_tip(grand_total)


# In[190]:


print(f'Tip Percent: {tip_percent*100}%')
print(f' Bill Total: ${bill_total}')
print(f'        Tip: ${round(tip,2)}')
print(f'Grand Total: ${round(grand_total,2)}')


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[ ]:





# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[ ]:





# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[ ]:





# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[ ]:





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

# In[ ]:





# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
# * cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# * cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[ ]:





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




