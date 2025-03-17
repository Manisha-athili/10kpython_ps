# 2. Second largest element or second smallest element in a given list


# method 01
given_list = [-4,-2,6,12,3,19]
list1= list(set(given_list))
def is_2ndlargest_2ndsmallest(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1[1],list1[-2]

print(is_2ndlargest_2ndsmallest(list1))


    
# approch 02
list1 = [-4,-2,6,12,3,1]
def is_2ndlargest_2ndsmallest(list1):
    max1 = 0
    min1 = list1[0]
    for i in list1:
        if i>max1:
            max1=i
    sec_max = 0
    for i in list1:
        if (max1>i and i>sec_max):
            sec_max=i
    print(max1,sec_max)
    return 

print(is_2ndlargest_2ndsmallest(list1))
    
    