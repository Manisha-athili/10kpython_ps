list1 = [1,2,3,4,5,6,3]

# for i in list:
#     print(i)

# for j in range(len(list)):
#     print(j)
#     print(list[j])

# iteration using while
# ind = 0
# while ind < len(list):
#     print(ind)
#     print(list[ind])
#     ind+=1

# find sum of elements in list
sum =0
for i in list1:
    sum += i
print(f"sum is {sum}")


# find min and max in list
max=list1[0]
min=list1[0]
for i in list1:
    if(max<i):
        max = i
    if(min>i):
        min = i  
print(max,min)

# # 2nd largest:
# for i in list:3
#     for j in list:
#         if i>j:
#             i,j=j,i
# print(list)


# finding the k element which is present in list
k= int(input("enter a number :"))
# edge case
list2 = [2,4,6,3,2,43]
if k>=-1*len(list2) and k< len(list2):
    print(list2[k-1])






