# WAP to perform the following task:
# input=[1,2,3,4,5,6]
# input=[3,4,5,6,7,8]
# OUTPUT=[4,6,8,10,12,14]
input1 = [1, 2, 3, 4, 5, 6]
input2 = [3, 4, 5, 6, 7, 8]
list = []
for i in range(0, 6):
    x = input1[i] + input2[i]
    list.append(x)
print(input1)
print(input2)
print(list)
