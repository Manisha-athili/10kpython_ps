# [1,3,4,5]
# [3,4,5,7]
# [9,8,7,5]


# sum of the matrix
matrix = [[2,5,3,4],[4,7,1,5],[3,0,5,8]]
print(matrix)
sum =0

for i in matrix:
    for j in i:
        sum +=j
print(sum)

print("or")
# print 1st row of the matrix
for i in matrix[0]:
    print(i,end=" ")

print("or")

# print all the elements of the matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

print("or")
# print border elements of the matrix

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==0 or j==0 or j == len(matrix[i])-1 or i == len(matrix)-1:
            print(matrix[i][j], end=" ")
        else: print(" ", end=" ")
    print()

print("or")
# print border elements of the matrix and sum of the border elements
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==0 or j==0 or j == len(matrix[i])-1 or i == len(matrix)-1:
            print(matrix[i][j], end=" ")
            sum += matrix[i][j]
        else: print(" ", end=" ")
    print()
    
print(sum)
print("or")

# print diagonal elements of the matrix and sum of the diagonal elements
sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j or i+j == len(matrix)-1:
            print(matrix[i][j], end=" ")
            sum += matrix[i][j]
        else: print(" ", end=" ")
    print()
    
print(sum)


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j or i == len(matrix)-1-j:
            print(matrix[i][j], end=" ")
            sum += matrix[i][j]
        else: print(" ", end=" ")
    print()
    
print(sum)

sum =0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j or i+j==len(matrix)-1:
            print(matrix[i][j], end=" ")
            sum += matrix[i][j]
        else: print(" ", end=" ")
    print()
    
print(sum)

sum =0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i==j or i+j==len(matrix)-1:
            print(matrix[i][j], end=" ")
            sum += matrix[i][j]
        if i==j and j +1==len(matrix)-1:
            print(matrix[i][j], end=" ")
            sum += matrix[i][j]
        else: print(" ", end=" ")
    print()
    
print(sum)


# minimum and maximum values in a nested list
        


