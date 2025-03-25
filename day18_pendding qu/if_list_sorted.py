# list1 = [-20,20,40,50,90,70]
list1 = [50,30,10]


def is_ass(list1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            return False
    return True
        
def is_des(list1):
    for i in range(len(list1)-1):
        if list1[i]<list1[i+1]:
            return False
    return True

def is_sorted(list1):
    return  is_des(list1) or is_ass(list1)
        

print(is_sorted(list1))