# print the following pattern
#     **
#    ***
#      *
#   ****
#  *****
# ******

n = int(input('Enter number of rows'))
spc = 5
star = 1
for i in range(0, n+1):
    for j in range(0, spc):
        print(' ', end='')
    for j in range(0, star):
        print('*', end='')
    print()
    star += 1
    spc -= 1
