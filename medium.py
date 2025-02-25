# Print the first 10 terms of the Fibonacci series using a  for loop. 
# f(n) = f(n-1)+f(n-2)
# a =0
# b = 0
# a+b
n=10
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(n-1):
    tem = num1 + num2
    print(tem)
    num1 = num2
    num2 = tem

# Check if a given number is a prime number using a  for loop. 
flag = 0
num = 99
if num in [0,1]:
    print("not a prime")
else:
    for i in range(1,num+1):
        if num%i==0:
         flag+=1
    print("prime")if flag == 2 else print("not print")
# here we inclued 1 and itself so flag == 2 only
# no. of iterations 16 // num time in worst


print("2nd Approche")


spy = True
# num=5
if num in [0,1]:
   print("not a prime")
else:
    for i in range(2,num):
      if num%i==0:
         spy = False
         break
    print('not a prime')if spy == False else print("prime")
# here w r not taking 1 and itsel num so no factor will come
# no of iterations will less due to using of break...
# num-1

print("3rd Approche")
spy = True
# num=5
if num in [0,1]:
   print("not a prime")
else:
    for i in range(2,num//2+1): # it exculdes half of the numbers
      if num%i==0:
         spy = False
         break
    print('not a prime')if spy == False else print("prime")
#16:2,4,8,16
#18:2,3,4,

# num/2 times in worst


   
print("4rd Approche")
spy = True
# num=5
if num in [0,1]:
   print("not a prime")
else:
    for i in range(2,int(num**0.5)+1): # root int add bcz to avoid float vals and 1 added as upper bond elimts
      if num%i==0:
         spy = False
         break
    print('not a prime')if spy == False else print("prime")
# root of n times in worst case



       
   
   