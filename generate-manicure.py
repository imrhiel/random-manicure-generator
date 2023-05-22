# Author : imriel <enki@faloran.fr>
# This is the main script for the random manicure generator

import random

# Defining our polishes lists
base_type = ['creme', 'linear', 'multichrome']
taco_type = ['glossy', 'matte']

# Select a random nail polish from the list
def select_random_polish(polish_type) :
    i = random.randint(0,len(polish_list)-1)
    polish = polish_list[i]
    return(polish)

# Import polishes list from text file
def import_list(polish_type):
    polish_list =  open('%s.txt' % polish_type).read().split('\n')
    return(polish_list)

print('Welcome to the Random Manicure Generator!\n')

# Randomly select base polish
i = random.randint(0,len(base_type)-1)
base = base_type[i]
print('Your base type is : %s' % base)
polish_list = import_list(base)
polish = select_random_polish(base)
print('Your random polish is : %s\n' % polish)

# Select topper if needed
input_topper = input("Do you wish to roll for a topper? (Y/n, defaults to yes):")
if input_topper.lower() == 'y' or  input_topper == '':
    polish_list = import_list('topper')
    topper = select_random_polish('topper')
    print('Your topper is: %s' % topper)

# Select taco if needed
input_taco = input("Do you wish to roll for a taco (top coat)? (y/n):")
if input_taco.lower() == 'y':
    taco = taco_type[random.randint(0,len(taco_type)-1)]
    print('Your taco is: %s' % taco)
else:
    print('Please still use a taco!')

exit 0
