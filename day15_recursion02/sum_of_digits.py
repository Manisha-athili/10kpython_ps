
num = 234

def sum_digit(num):
    if num<=0:
        return 0
    return (num%10)+sum_digit(num//10)

print(sum_digit(num))