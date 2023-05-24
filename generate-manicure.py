# Author : imriel <enki@faloran.fr>
# This is the main script for the random manicure generator

import random

# Defining our polishes lists
base_type = ['creme', 'linear', 'multichrome']
taco_type = ['glossy', 'matte']

# Randomly selecting on a list
def roll_polish(polish_type) :
    return polish_type[random.randint(0,len(polish_type)-1)]
    

# Select a random nail polish from the list
def select_random_polish(polish_type) :
    polish_list =  open('files/%s.txt' % polish_type).read().strip('\n').split('\n')
    polish = roll_polish(polish_list)
    return(polish)

print('Welcome to the Random Manicure Generator!\n')

# Randomly select base polish
base = roll_polish(base_type)
print('Your base type is : %s' % base)
polish = select_random_polish(base)
print('Your random polish is : %s\n' % polish)

# Select topper if needed
input_topper = input("Do you wish to roll for a topper? (Y/n, defaults to yes):")
if input_topper.lower() == 'y' or  input_topper == '':
    topper = select_random_polish('topper')
    print('Your topper is: %s' % topper)

# Select taco if needed
input_taco = input("Do you wish to roll for a taco (top coat)? (y/n):")
if input_taco.lower() == 'y':
    taco = roll_polish(taco_type)
    print('Your taco is: %s' % taco)
else:
    print('Please still use a taco!')

exit(0)
