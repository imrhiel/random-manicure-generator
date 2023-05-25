# Author : imriel <enki@faloran.fr>
# This is the main script for the random manicure generator

# ------------------------------ INITIALIZING ------------------------------

import os
import random
from pathlib import Path

# Defining our polishes lists
base_type = ['creme', 'linear', 'multichrome']
taco_type = ['glossy', 'matte']

list_path = 'files'

# Randomly selecting on a list
def roll_polish(polish_type) :
    return polish_type[random.randint(0,len(polish_type)-1)]
    
# Select a random nail polish from the list
def select_random_polish(polish_type) :
    polish_list =  open('%s/%s.txt' %(list_path,polish_type)).read().strip('\n').split('\n')
    polish = roll_polish(polish_list)
    return(polish)


# --------------------------------- MAIN SCRIPT --------------------------------

print('Welcome to the Random Manicure Generator!\n')
choice = input("What do you want to do?\n1. Roll for full manicure\n2. Roll on a specific list\nYour choice (1 or 2): ")

# Roll for full manicure
if choice == '1':
    # Randomly select base polish
    base = roll_polish(base_type)
    print('\nYour base type is: %s' % base)
    polish = select_random_polish(base)
    print('Your random polish is: %s\n' % polish)

    # Select topper if needed
    input_topper = input("Do you wish to roll for a topper? (Y/n): ")
    i = 1
    while i == 1:
        if input_topper.lower() == 'y' or  input_topper == '':
            topper = select_random_polish('topper')
            print('Your topper is: %s' % topper)
            i+=1
        elif input_topper.lower() =='n':
            i+=1
        else:
            input_topper = input("Please type y or n: ")

    # Select taco if needed
    input_taco = input("Do you wish to roll for a taco (top coat)? (y/N): ")
    i = 1
    while i == 1:
        if input_taco.lower() == 'y':
            taco = roll_polish(taco_type)
            print('Your taco is: %s' % taco)
            i+=1
        elif input_taco.lower() == 'n' or input_taco == '':
            print('Please still use a taco!')
            i+=1
        else:
            input_taco = input("Please type y or n: ")


# Roll on one specific list
elif choice == '2':
    # List available choices
    print("\nYou can select one of these types:")
    for i in os.listdir(list_path):
        print(Path(i).stem)

    # Get desired type
    polish_type = input("\nPlease enter the selected type and hit Enter: ")
    
    i = 1
    while i == 1:
        # If the input is an existing list, select polish
        if polish_type+'.txt' in os.listdir(list_path):
            polish = select_random_polish(polish_type)
            print('Your random polish is: %s' % polish)
            i += 1
        # The list doesn't exist
        else:
            polish_type = input('Sorry, this type of polish is not available. Try again: ')


exit(0)
