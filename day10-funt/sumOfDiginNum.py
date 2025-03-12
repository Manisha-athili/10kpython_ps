# WAP to find the sum of digits for each number in the list
# inp_list = [202,89,112,88] => [4,17,4,16]

inp_list = [202,89,112,88]
new_list = []

def sumOfdigit(num):
    sum = 0
    while(num>0):
        digit = num%10
        num = num//10
        sum += digit
    return sum
# sumOfdigit(202)

for i in inp_list:
    new_list.append(sumOfdigit(i))
print(new_list)
    
# WAP to find the sum of digits if it is even only for each number in the list
# inp_list = [202,89,112,88] => [4,17,4,16]
print("Try programiz.pro")
inp = [202,89,-112,88]
new_list = []

def sumOfdigit(num):
    sum = 0
    while(num>0):
        digit = num%10
        num = num//10
        sum += digit if digit%2==0 else False
    return sum
# sumOfdigit(202)

for i in inp:
    new_list.append(sumOfdigit(i))
print(new_list)

# WAT that returns True if any digit is repeated in the number
# inp_list = [202,89,112,88] => [True,False,True,True]
# separate the digits and store them in list
inp = [202,89,112,88]
new_list = []

def sumOfdigit(num):
    digit_list = []
    while(num>0):
        digit = num%10
        num = num//10
        if digit in digit_list:
            return True
        else:
            digit_list.append(digit)
    return False
# sumOfdigit(202)

for i in inp:
    new_list.append(sumOfdigit(i))
print(new_list)
print("====================================")



# WAP list1 is subset of list2
# arr1 = [1,2,3,4,5] 
# arr2 = [2,3,4,5,32,1,23,43]
arr1 = [1,2,3,4,5] 
arr2 = [2,3,4,5,32,1,23,43]
def isArrSubset(arr1,arr2):
    for i in arr1:
       if i not in arr2:
           return "not a Subset"
    return "subset"
    
print(isArrSubset(arr1,arr2))

    