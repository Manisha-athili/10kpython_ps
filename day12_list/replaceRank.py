# 3. Given array of N integer, the task is to replace each element of the array  by its rank in the array
#    Input: 20 15 26 2 98 6
            # 2   6  15 
#    Output:4 3   5   1  6 2

list1 =[20,15,26,2,98,6]
list1.sort()
temp_list = list1
# sort_list = new_list.sort()
print(temp_list)

int_list = [20,15,26,2,98,6]
rank_list =[]
for i in int_list:
    max1 = 0
    for num in int_list:
        if num>max1:
            max1=num
    print(max1)
    rank_list.index(max1)=i
    int_list.remove(int_list.index(max1))
print(rank_list,int_list)


