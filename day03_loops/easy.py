# . Loops easy level:: 
# Print all numbers from 1 to 100 using a  for  loop. 
# for i in range(0,100):
#     print(i+1)

# Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2).... n/s(n+1)

n = 10
sum = n*(n+1)
print(sum/2)

def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is:", sum_natural_numbers(n))
