# take number input from user
#input= 1037
#output = 1537
#input = 110305
#output = 115355
from re import A


num = input("Enter a number")
temp = num
temp = ''
for i in num:
    if(i == '0'):
        temp = temp+'5'
    else:
        temp = temp + i
print(temp)
