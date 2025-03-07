#9. WAP find sum of odd in number ip : 2355 out:: 13
num = 2355
sum =0
tem = num
while tem>0:
    digit = tem%10
# print()
    if(digit)%2 != 0:
        sum += digit
    tem = tem//10
print(sum)

# reverse a number ip = 2345
num = 2345
reverse=0
temp = num
while temp!=0:
    temp%10
    reverse =  reverse*10+ (temp%10)
    temp= temp//10
    print(reverse)

