"""
This is a program to print the first 20 fibonacci numbers

Author:- Souparna Nath

Date:- 05.11.2019
"""

first = 0
second = 1

print (first)
print (second)

for i in range(20):
    third = first + second
    print (third)
    first = second
    second = third
