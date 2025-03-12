# 4. Missing even numbers in the list in between max and min even numbers in the list
list1 = [-4,-2,6,10,12]

# min1 = min(list1)
# max1 = max(list1)

def missing_num(list1):
    min1 = list1[0]
    max1 = 0
    for i in list1:
        if i<min1:
            min1 = i
        elif i>max1:
            max1 = i
    print(max1,min1)

    for num in range(min1,max1+1):
        # print(num)
        if num not in list1:
            print(num)
    return            #none returns
missing_num(list1) # we are not printing