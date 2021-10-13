import random
import sys

print('palam polom')


while True:
    comp1 = random.randint(1, 2)
    comp2 = random.randint(1, 2)
    
    
    user = int(input('please enter your choose :'))
    if comp1==comp2 and comp1!=user :
        print('user lose!!')
    elif comp1==user and comp1!=comp2 :
        print('computer 2 lose ')
    elif comp2==user and comp2!=comp1 :
        print('computer 1 lose ')
    elif comp1==comp2==user:
        print('All the gamer same\nDo it again')
    elif user!=1 or user!=2 :
        
        
        print('Select evidence number 1 and 2')
        
        sys.exit(0)