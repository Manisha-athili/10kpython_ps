# 1. Find the missing numbers - In the between max and min digits in the given inputs, find the missing digits.
# Input: 34571      Outpur : 26 missing

num = 34571 
temp = num
def missing_digit(temp):
    list = []
    while(temp>0):
        digit = temp%10
        temp = temp//10
        list.append(digit)
    max1 = max(list)
    min1 = min(list)
    for i in range(min1,max1+1):
        if i not in list:
            print(i)
    return
missing_digit(num)

