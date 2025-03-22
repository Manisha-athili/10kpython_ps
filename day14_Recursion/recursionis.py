# what is recursion?
# A function calling the same function with different arguments (keep calling itself)...stops when Base case is triggered

# if no base case --> maximum recursive depth exceeded-->error by cpu when limit crossed-+++++++

# find factorial of 5

n = 5
def fact(n):
    if n==1 or n==0:
        return 1
    return n * fact(n-1)
print(fact(n))

def printer(n):
    if n==1 or n==0:
        return
    print(n)
    printer(n-1)
    print(n)
printer(10)

# 10 => F => print 10 => call(9) => condition F => print 9 => call (8) => condition f => print 8 => call (7)=> condition(F) = print 7 => call(6) => condition(f) => print 6 => call(5) => condition (f) => print 5=> call(4) => condition(F) =>print 4
# call 3 => condition(f) => print 3 => call(2) => condition(f)=>  print(2) => call(1) => condition(t) :: return non 

# non stores in 1 and prints 

# print  1 to n numbers without for loops and multiple print statements

def num(n):
    if n == 0:
        return 
    num(n-1)
    print(n)

num(10)

# febino
0,1 ,1,2,3,5
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(5))

# 3. Sum of digits

def sum(n):
    if n==0:
        return n
    return n + sum(n-1)
print(sum(4))

# 5. Exponent

def ex(base,power):
    if power ==0:
        return 1
    return base * ex(base,power-1)
print(ex(2,3))

# 6. Check if string is a palindrome




