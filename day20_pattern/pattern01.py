# 1
# 2 3
# 4 5 6
# 7 8 9 10


num = 4
count = 1
for i in range(num+1):
    for j in range(num+1):
        if i>=j:
            print(count, end="  ")
            count +=1
    print()


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

print("shut your mouth")
