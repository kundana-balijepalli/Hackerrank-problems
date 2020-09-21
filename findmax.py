#This program finds the maximum number from an input of 5 nums given from the user.

import sys

#take user input
a = input("Enter 4 values")
ans = a.split(',')
#a = sys.argv[1].split(',')
print(max(a))