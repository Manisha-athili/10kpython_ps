# n = 4
# for i in range(n):
#     for j in range(0,n):
#         if j==n-i:
#             print("*",end=" ")
#     print()



num = 4
for i in range(num+1):
    for j in range(num+1):
        if i<=j:
            print(" ", end=" ")
    for j in range(num+1):
        if i>=j:
            print("*", end=" ")
    for j in range(num+1):
        if i>j:
            print("*", end=" ")
    print()

# for i in range(n):
