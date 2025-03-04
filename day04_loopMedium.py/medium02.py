# WAP to calculate the factorial of a number using a  while  loop. 

num = 5  # 5*4*3*2*1
fact = 1
while num>=1 :
    fact *= num
    num-=1
print(fact)
    
# num = 5
# fact = 1  # Start from 1, as factorial of 0 is 1

# while num >= 1:
#     fact *= num  # Multiply fact by num
#     num -= 1  # Decrement num

# print(fact)  # Print final factorial value
# 


# print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop.

for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

#Implement a menu-driven program where the user can 
# choose to: 
# 1.  Find the square of a number. 
# 2.  Find the cube of a number. 
# 3.  Exit. 

print("---")
a = [1,2,3,4,5,6,7,8]
print(a)
for i in a:
    a.remove(i)
    print(a)
print(a)
# iteration length/2

