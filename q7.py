# ask a user to enter any number and test weather it is pallindrome or not?
num = int(input('Enter any number to check'))
temp = num
n = 0
while(num > 0):
    digit = num % 10
    n = n * 10 + digit
    num = num//10
if(temp == n):
    print('pallindrom')
else:
    print('Not pallindrom')
