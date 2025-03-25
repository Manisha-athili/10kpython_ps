# 1. swapping 

# approch 01
a,b = 10 , 20

# approch 02
temp = a
a = b
b = temp
print(a,b)

# approch 03 if numbers only
a = a+b
b = a-b
a = a-b
print(a,b)

# xor ^  0,0 = 0 1,1 = 0,  0,1 = 1 ,
# num1 ^ num1 = 0
# num1 ^ 0 = num1

# approch 04 if numbers only
a = a^b # 10 ^20
b = a^b # 10^20^10
a = a^b #  10^20^20
print(a,b)



