# b.  Medium Questions: 

# 1. Write a program to find the greatest of three numbers.
num1 = int(input('Enter a num1: '))
num2 = int(input('Enter a num2: '))
num3 = int(input('Enter a num3: '))

if num1>num2 and num1>num3:
    print('num1 is greatest')
elif num2>num1 and num2>num1:
    print('num2 is greatest')
elif num3>num1 and num3>num2:
    print('num2 is greatest')   
else:print('equal')

# 2. Check if a year is a leap year. 
year = int(input('Enter year to check leap year or not: '))
# if year%4==0:
#     if year %100==0:
#         if year%400==0:
#             print('leap year')
#         else:print('common year')
#     else:print('leap year')
# else:print('Common Year')
print('or')
if (year%4==0 and year % 100==0)or year % 400 ==0:
    print('leap year')
else:print('Common Year')


# 3.WAP T  classify a character entered by the user as a vowel, consonant, or neither. 
c = input('Enter a character: ').lower()
if (c == 'a' or c == 'e' or c == 'i' or c== 'o' or c == 'u'):
    print('Vowel')
elif(c == 'b' or c == 'c' or c == 'd' or c == 'f' or c == 'g' or c=='h' or c == 'j' or c == 'k' or c == 'l' or c== 'm' or c == 'n' or c == 'p' or c == 'q' or c == 'r' or c== 's' or c == 't' or c == 'v' or c == 'w' or c == 'x' or c == 'y' or c == 'z'):
    print('Consonant')
else:print('neither consonant nor vowel')

# 4 Calculate the grade of a student based on the marks they 
# score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. 

marks = float(input('Enter your marks: '))
if(marks <70): 
    print('Fail')
elif(marks >=70 and marks <= 79):
    print('Grade C')
elif(marks>=80 and marks <=89):
    print('Grade B')
elif(marks>= 90 and marks <= 100):
    print('Grade A')


# WAP to check if three sides length form a valid 
# triangle. 
a = float(input('Enter 1st side of triangle'))
b = float(input('Enter 2nd side of triangle'))
c = float(input('Enter 3rd side of triangle'))

if(a+b>c and a+c>b and c+b>a):
    print('Valid')
else:print('Not a vaild triangle')