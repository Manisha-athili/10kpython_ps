# 1) choose to an operation to perform : 
# 1. Find the square of a number.
# 2. Find the cube of a number. 
# 3. Exit.
# 2) check a number is palindrome or not
# 3) check a number is perfect or not
# 4) find LCM(Least Common Multiple) of two numbers
# 5) calculate total allocated budget for all even numbered Teams members



# . Implement a menu - driven program when the user can choose to:
#    1. Find the square of a number
#    2. Find the cube of a number
#    3. Exit

num = int(input("Enter a Number"))
choice  = int(input("Enter a number from 1 to 3"))
while True:
    if choice == 1:
        print("The square of", num, "is:",num ** 2)
        False
        break
    elif choice == 2:
        print("The cube of", num, "is:", num ** 3)
        False
        break
    elif choice == 3:
        False
        break
    else:
        print("Enter the choice from 1 to 3 only")
        break



# check palindrome or not
num = int(input("Enter a number to check palindrome or not"))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if temp == rev:
    print(rev,"It is a Palindrome Number")
else:
    print(rev,"It is not a Palindrome Number")


# check perfect number or not:
num = int(input("Enter a number to check perfect number or not:"))
sum = 0
i = 1 
print("The divisors of", num, "are:", end=" ")
while i<num:
    if num % i == 0:
        print(i,end=" ")
        sum = sum + i
    i += 1
if sum == num:
    print("\n",num, "is a perfect number")
else:
    print("\n",num, "is not a perfect number")



# GCD of two numbers
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
while b > 0:
    rem = a % b
    a = b
    b = rem
GCD = a
print("GCD of two numbers is:", GCD)

# LCM of two numbers 
x = int(input("Enter the first number:"))
y = int(input("Enter the second number"))
if x > y:
    big = x
else:
    big = y
while True:
    if (big % x == 0) and (big % y == 0):
        LCM = big
        break
    big = big + 1
print("LCM of two numbers is:", LCM)

