# wap to ask to input salary and on terminal print the tax that needs to be paid cosidering the situation salary #above 10 lakh tax is 30%, salary between 5lakh to 10 lakh then slab is 20% and in case salary is less than 5 #lakh then no tax.
salary = float(input('Enter your salary'))
if(salary > 100000):
    tax = salary*(30/100)
    tax = str(tax)
    print('You have to pay', tax, 'tax based on your salary')
elif(salary >= 500000 and salary <= 100000):
    tax = salary * (20/100)
    tax = str(tax)
    print('You have to pay', tax, 'tax based on your salary')
else:
    print("you don't have to pay any tax")
