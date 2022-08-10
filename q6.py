# Ask user to enter a number test whether it is armstrong number or not
num = int(input("enter a number to check :"))
temp = num
res = 0
while(num > 0):
    rem = num % 10
    res = res + (rem*rem*rem)
    num = num//10
if(temp == res):
    print('armstrong')
else:
    print('Not armstrong')
