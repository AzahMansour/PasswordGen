#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string  #this will grab all the upper and lowercase letters, numbers, and special characters that exist

def generate_password(min_length, numbers = True, special_characters = True): #user will state minimum length for password and if they was numbers & special characters (criteria)
    letters = string.ascii_letters   
    digits = string.digits  
    special = string.punctuation   # these variables have been assigned all the potential characters we could use (letters, nums, special characters

    characters = letters #there will always be letters in all passwords
    if numbers:
        characters += digits #if numbers=True the digits string will be added to character(letter) string 
    if special_characters:
        characters += special #if special_characters=True the special string is added to character(letter) string

    #starting a loop, every iteration of loop will generate new character to add to randomized password until all criteria from function are met
    pwd = ""  #stands for password, where password will be stored (empty right now)
    meets_criteria = False  #will be set to True once criteria met
    has_num = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:  #condition for while loop: while we are not meeting criteria, loop will continue adding characters
        new_char = random.choice(characters) #generates new character
        pwd += new_char #adds new character to password

#determines if the character generated was a number or special character
        if new_char in digits:  #if exists in digits, then the number criteria met
            has_num = True
        elif new_char in special:
            has_special = True    #if exists in special, the the special character criteria met

        meets_criteria = True
        if numbers:  #if we should include a number, and there is a number meets_criteria stays True, else False
            meets_criteria = has_num  
        if special_characters: #if we should included a special character, and there is a special char, then meets_criteria stays True, else False
            meets_criteria = meets_criteria and has_special  #will be set to False if meets_criteria and has_special aren't both True

    return pwd  #password returned when all criteria met

min_length = int(input("Enter the minimum length: "))
has_num = input("Do you want to include numbers? (yes/no): ").lower() == "yes"  #if user types anything other than yes (no), number/special char wont be included
has_special = input("Do you want to include special characters? (yes/no): ").lower() == "yes"  # == checks for equivalence
pwd = generate_password(min_length, has_num, has_special)
print("The generated password is: ", pwd)


# In[ ]:




