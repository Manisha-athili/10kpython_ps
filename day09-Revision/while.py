# i = 1
# while i<=50:
#     if i%2==0:
#         print(i)
#     i += 1    
   
# i = 2
# while i<=50:
#     print(i)
#     i += 2   

# multiplication

# i = 1
# while i<=20:
#     j = 1
#     while j<=10:
#         print(f"{i} * {j} = {i*j}")
#         j += 1
#     print("********",i)
#     i += 1

# print("reverse a number and print sum")

# num = 2546
# sum = 0
# while num>0:


num = int(input("enter n number : "))
for num1 in range(0,5):
    i = 1
    while i<=num:
        print("* ",end="")
        i +=1
    print()
    
num = int(input("enter n number : "))
for num1 in range(0,5):
    for i in range(0,num1+1):
        print("* ",end="")
    print()
    
    
    