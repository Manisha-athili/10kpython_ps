# And also find the time complexity and space complexity for all problem solving questions


#1
num = input("Enter a number")
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is equal to zero")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")



# 2

num = input("Enter a number")
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")



# 3

age = input("Enter the age")
result = "Eligible to vote" if age>=18 else "Not Eligible to vote"
print(result)
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")

# 4

num1 = input("Enter first number")
num2 = input("Enter second number")
result = "num1 is greater" if num1>num2 else "num2 is greater"
print(result)
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")



# 5

marks = input("Enter the marks")
if marks>'40':
    print("Pass")
else:
    print("Fail")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 6
number = input("Enter a number")
if number == '1':
    print("Monday")
elif number == '2':
    print("Tuesday")
elif number == '3':
    print("Wednesday")
elif number == '4':
    print("Thursday")
elif number == '5':
    print("Friday")
elif number == '6':
    print("Saturday")
elif number == '7':
    print("Sunday")
else:
    print("Not valid")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")



# 7
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
inp = input("Enter an operation").lower()
if inp in ['add', '+']:
    print(num1+num2)
elif inp in ['sub', '-']:
    print(num1-num2)
elif inp in ['mul', '*']:
    print(num1*num2)
elif inp in ['div', '/']:
    if num2 == 0:
        print("Div with 0 is not possible")
    else:
        print(num1/num2)
else:
    print("Invalid Input")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 8
month = int(input("Enter a number"))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")



# 9

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
if num1 > num2 and num1 > num3:
    print(num1, "is greater number")
elif num2>num1 and num2 > num3:
    print(num2, "is greater number")
elif num3 > num1 and num3 > num2:
    print(num3, "is greater")
else:
    print("All three are equal numbers")

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 10

year = int(input("Enter a year"))
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 400 == 0) and (year % 100 == 0)):
    print("Leap Year")
else:
    print("Not a Leap year")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


#  11
def alphabet(char):
    vowels = "aeiouAEIOU"
    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "neither"
    
char = input("Enter a single character")
if len(char) == 1:
    result =alphabet(char)
    print(result)
else:
    print("Enter single character only")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 12
marks = int(input("Enter marks"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks <=89:
    print("Grade B")
elif marks >= 70 and marks <=79:
    print("Grade C")
elif marks < 70:
    print("Fail")
else:
    print("Not a number")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 13
a = int(input("Enter the length of side 1: "))
b = int(input("Enter the length of side 2: "))
c = int(input("Enter the length of side 3: "))
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("It will form a valid triangle")
else:
    print("It will not form a valid triangle")
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 14
for i in range(1, 101):
    print(i)

print("Time Complexity:", "O(n)")
print("Space Complexity:", "O(1)")


# 15
n = 50
print((n*(n+1))/2)
def func(n):
    print((int)(n*(n+1)/2))

func(50)
print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 16
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i+=1
print("Time Complexity:", "O(n)")
print("Space Complexity:", "O(1)")


# 17

num = int(input("Enter a number"))
for i in range(1, 11):
    print(num, "*", i, "=", (num*i))

print("Time Complexity:", "O(1)")
print("Space Complexity:", "O(1)")


# 18


num = 54327
rev = 0
sum = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
    sum += rem
print(rev)
print(sum)

print("Time Complexity:", "O(logn)")
print("Space Complexity:", "O(1)")


# 19

num = 12345
count = 0
while num > 0:
    rem = num % 10
    count += 1
    num = num // 10

print(count)

print("Time Complexity:", "O(logn)")
print("Space Complexity:", "O(1)")



# 20
while True:
    number = int(input("Enter a number"))
    if number < 0:
        break

num1 = 0
while num1 >= 0:
    num1 = int(input("Enter non negative number only"))

print("Time Complexity:", "O(k+m)")
print("Space Complexity:", "O(1)")