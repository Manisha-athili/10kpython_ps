# Wap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not
input= [568,89,112,88,571]     
# Output: [true,true ,false,false ,false]

def is_digit_incresing(num):
    temp = num
    prev_num=10
    while(temp>0):
        digit = temp%10
        temp = temp//10
        # print(digit)
        if digit>=prev_num:
            return False
        prev_num=digit
    return True
list1 = []
for num in input:
    list1.append(is_digit_incresing(num))
print(list1)


