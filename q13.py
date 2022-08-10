# get a list of items from user swap the first and last number and print the final list as output of the program
from tempfile import tempdir


list = []
temp = 0
n = int(input("Enter the length of List: "))
for i in range(0, n):
    a = int(input("Enter number"))
    list.append(a)
temp = list[0]
list[0] = list[n-1]
list[n-1] = temp
print(list)
