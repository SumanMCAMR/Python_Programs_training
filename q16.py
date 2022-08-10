# take a list as input from user and output the following:
from operator import truediv
from re import M
from unittest.util import sorted_list_difference


list = []
n = int(input('enter the list size'))
for i in range(0, n):
    m = int(input("inter Number: "))
    list.append(m)
print(sorted(list))
print(sorted(list, reverse=True))
