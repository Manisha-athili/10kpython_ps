# Week 01 topic Conditional statements , for while (max 2 days)

# 1. if else and if-else ladder
# easy:

# 1 WAP to check if a num is +ve , -ve or zero
num = float(input("Enter a number: "))
if num > 0:
    print("your number is positive")
elif num<0:
    print("your number is negative")
else:
    print("your number is zero")
# 2. determine if a number is odd or even
if num%2==0:
    print('even')
else: print('odd')
# 3. C if a person is eligible to vote(age>=18)
age = int(input("Enter your Age: "))
if age>= 18:
    print("you are eligible to vote",age)

# 4. WAP to find the greatest of 2 numbers.
num1 = 55;
num2 = 5;
if num1>num2:print('num1 is greatest',num1)
else:print('num2 is greatest',num2)

# 5. print "pass if a student scores more than 40 marks, otherwise print "Fail
score = float(input('Enter your Score: '))
if score > 40 : print("Pass")
else: print("Fail")

# 6.WAP to display the day of the week based on a  number input (1 for Monday, 2 for Tuesday, etc.). 
day = int(input('Enter a number bt 1 to 7: '))
if day == 1 : print("Monday")
elif day == 2 : print("Tuesday")
elif day == 3 : print("Wednesday")
elif day == 4 : print("Thursday")
elif day == 5 : print("Friday")
elif day == 6 : print("Saturday")
else: print('Sunday')
print("or")
# arr = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# for i in arr:
#     if day==i :
#         print(arr[i])
   

# 7. implement a simple calculator to perform addition, subtraction, multiplication, and division. 
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
operator = input("Enter the operator: ")
if operator == '+':
    print(a+b)
elif operator == '-':
    print(a-b)
elif operator == '*':
    print(a*b)
elif operator=='/':
    print(a/b)

# 8. WAP to display the name of a month based on the month number (1 for January, 2 for February, etc.).
month = int(input('Enter a number 1 to 12: '))
if  month == 1:print('January')
elif month == 2:print('February')
elif month == 3:print('March')
elif month == 4:print('April')
elif month == 5:print('May')
elif month == 6:print('June')
elif month == 7:print('July')
elif month == 8:print('August')
elif month == 9:print('September')
elif month == 10:print('October')
elif month == 11:print('November')
elif month == 12:print('December')
