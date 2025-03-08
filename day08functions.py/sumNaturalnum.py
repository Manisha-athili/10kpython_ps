# sum of 10  natual number  10 + 9 +8+ 7
num = 10
def sum_natural(inp_num):
    sum = 0
    num1 = 1
    while num1<=inp_num:
        sum = sum + num1
        num1 += 1
    return sum
print(sum_natural(num))



