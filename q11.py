# print the following pattern:
# approch by sir
n = int(input("Enter row count"))
for i in range(0, n):
    for j in range(0, i):
        print('*', end='')
    print('')

# approch by me
n = int(input("Enter number"))
for i in range(0, n):
    s = '*'
    print(i*s)
