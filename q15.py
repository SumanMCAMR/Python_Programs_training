# wap to display month and days for entered number of days by the user
m = int(input('enter days'))
month = m//30
day = m % 30
print(f" {month} month {day} day ")
