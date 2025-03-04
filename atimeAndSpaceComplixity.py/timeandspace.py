#TIME COMPLEXITY:::
#  raw time is not a matric to compare a time Complexicity... it also depends on computer version, processer, ,,,ect
# so we consider NUMBER OF OPERATIONS



# using loops
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is:", sum_natural_numbers(n))
# no of operations: ---> n no.of operations
# time complxity:: liner time complexity: no. of input == no. of operations
# t.c = O(n)
# space ---> 



# using formula

print((n*(n+1))/2)
# no of operations: ---> 1 single arthimatical operation
# time : constant time , parallel to x asix, y=x
# T>C : constant time complexity ==> O(1)

# space ---> 

num1 = 10
for i in range(1,num1+1):
    for j in range(1,num1+1):
        print(i,j)

# input 10 - oper 100
# inp 100 - oper 10000
#t.c O(n squ)

# O(1) < O(n) < O(nsq) < O(n cube) 

# O(1) <O(logn) < O(n)< O(nlogn)< O(nsq)< O(n cube)
# 
#  
# 
# 
# 
# MEMORY COMPLEXITY : Space Complexity::
# RAM and ROM : we have limited space for RAM ..programs runs in RAM...

# O(1)      - constant MC
# O(n)      - constant MC
# O(n sq)   - 

l1 = [1,3,4,5,1,2,4.5,3,2,7,9]
du_l1 = []

# for i in l1:
#     if i not in du_l1:
#         li