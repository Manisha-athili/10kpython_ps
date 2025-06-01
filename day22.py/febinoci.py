# 0 
# 1 1 
# 2 3 5 
# 8 13 21 34 
# 55 89 144 233 377 

a =0
b = 1
num =4
for i in range(num+1):
    for j in range(num+1):
        if(i>=j):
            print(a,end=" ")
            # tem = a+b
            # a=b
            # b=tem
            a,b = b,a+b
    print()

num =4

for i in range(num+1):
    a = 65
    for j in range(num+1):
        if(i>=j):
            print(chr(a), end=" ")
        a+=1
    print()
 
        