#will import from module.py
#import module ---> module.is_kendra()
#from module import is_kendra() ---> is_kendra() scope is limited to only this function here 
import module as md # ---> md.is_kendra()
import sys

#few common standard libary modules
import random as rd
import math
import datetime
import calendar
import os

#LMAO
## import antigravity




print(datetime.date.today())
print(calendar.isleap(2024))

print(math.sin(math.radians(90)))

print(os.getcwd())

print(os.__file__)


print("----------------------------------------------------------------------")

#nums = [2,3,4,5,6,7,8,9,10,11,12]
nums = [0]


for x in nums:
    if x == 0:
        print('bye bye')
        break
    if md.is_kendra(x):
        print(f'{md.is_kendra(x)}, the number {x} is in kendra.')
    elif x == 5 or x == 9:
        print(f'the number {x}, is in kona')
    elif x == 6 or x == 8 or x == 12:
        print(f'{x} is in dusthana')
    else:
        print(f'the number {x} is not in kendra, trikona, nor dusthana')

'''
for x in sys.path:
    print(x)

'''

num_list = ['1','2','3','4','5','6','7','8','9','10','11','12']

random_num = rd.choice(num_list)
print(random_num)
