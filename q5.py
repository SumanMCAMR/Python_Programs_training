# Ask user to enter 10 number. output of code should be max number, min number and avg value.
list = []
for i in range(0, 10):
    x = int(input('Enter numbers'))
    list.append(x)
print(list)
print(max(list))
print(min(list))
print(sum(list)/10)
