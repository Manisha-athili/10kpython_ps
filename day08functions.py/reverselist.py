# revers a list using empty list

list1 = [1,2.3,45,True]
def reverse_list(input_list):
    new_list = []
    # for i in input_list:
    #     new_list.insert(0,i)
    for i in range(len(input_list)-1,-1,-1):
        new_list.append(input_list[i])
    return new_list

print(reverse_list(list1))

# without list::
def reverse_list_swap(input_list1):
    low = 0
    high = len(input_list1)-1
    while low<high:
        input_list1[low],input_list1[high]=input_list1[high],input_list1[low]
        low += 1
        high -= 1
    return input_list1
print(reverse_list_swap(list1))


# reversing half list

def reverse_list_swap(input_list1):
    low = int(len(input_list1)/2)
    high = len(input_list1)-1
    while low<high:
        input_list1[low],input_list1[high]=input_list1[high],input_list1[low]
        low += 1
        high -= 1
    return input_list1
print(reverse_list_swap(list1))

# ///// 

def reverse_list_swap(input_list1):
    low = 0
    high = (len(input_list1)-1)//2
    while low<high:
        input_list1[low],input_list1[high]=input_list1[high],input_list1[low]
        low += 1
        high -= 1
    return input_list1
print(reverse_list_swap(list1))



        

