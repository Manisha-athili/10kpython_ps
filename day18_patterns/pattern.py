n = 6

for i in range(n):
    for j in range(n):
        print("* " , end="")
    print()

print("or")
for i in range(n):
    print("* " * n)

    
# 0,0   0,1   0,2    0,3
# 1,0   1,1   1,2    1,3
# 2,0   2,1   2,2   

for i in range(n):
    for j in range(i):
        print("* " , end="")
    print()

for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
    print()

print("or")

for i in range(n):
    for j in range(n):
        if i>=j:
            print(" ",end=" ")
        else:print("+",end=" ")
    print()

print("---------------------------------------")
n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*" , end=" ")
    print()
for i in range(n-1):
    for j in range(n-1):
        if i<=j:
            print("*", end=" ")
    print()
print("---------------------------------------")

for i in range(n):
    for j in range(n):
        if (j==0 or i==0 or i == n-1 or j==n-1):
             print("*" , end=" ")
        else: print(" ", end=" ")
    print()

print("---------------------------------------")

for i in range(n):
    for j in range(n):
        if i == j or i +j ==n-1 or j==0 or i==0 or i == n-1 or j==n-1:
            print("*", end=" ")
        else: print(" ",end=" ")
    print()

print("---------------------------------------")

for i in range(n):
    for j in range(n):
        if i == j or i +j ==n-1 or i==0 or i==n-1:
            print("*", end=" ")
        else: print(" ",end=" ")
    print()

print("---------------------------------------")

for i in range(n):
    for j in range(n):
        if i == j or i +j ==n-1 or i==0 or i == n-1:
            print("*", end=" ")
        else: print(" ",end=" ")
    print()
