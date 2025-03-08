num = int(input("enter num"))

# function modularity : to divide code into small codes...

def reverse_number(inp_num):
    temp = inp_num
    rev_num = 0
    while temp>0:
        rem = temp%10
        rev_num = rev_num*10 + rem
        temp //= 10
    return rev_num
print(reverse_number(num))
result = reverse_number(num)


#  palindrom
def palindrome(inp_num):
    # result = reverse_number(num)
    if result == inp_num:
        return "palindrome"
    return "not a palindrome"

print(palindrome(num))

# ternary operator : 
# True if condition esle


# factorial :::  5! = 5*4*3*2*1
def check_factorial(input_num):
    if input_num < 0:
        return print('Invalid Input')
    i = 1
    result = 1
    while i<= input_num:
        result*=i
        i+=1
    return result
print(check_factorial(num))




