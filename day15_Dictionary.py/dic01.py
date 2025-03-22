{
    1:2,
    2:3,
    'string': 1,
    5: 6,
    'list': [1, 2, 3, 4],
    'dict': {
        'a': 1,
        'b': 2
    }
}
# this is a dictionary with keys and values
# the keys are integers, strings, and lists 
# the values are integers, strings, and dictionaries
# the dictionary is nested inside another dictionary
# the list is nested inside the dictionary vias versa

list1 = [1,3,-2,"string",5.5,2,3,2,7,62]
dic = {}


for i in list1:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

print(dic)

for i,j in dic.items():
    if j == 1:
        print(i , "is uniquc")
    else : print(i , "count is " ,j)

for i,j in list1:
    print("i is ",i,j)



list2 = []
  