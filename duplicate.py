# WAP to print duplicates and unique numbers in an list

list2 = [2,3,4,5,2,3,2,2.3,-1,-3,654,21,-3]
dup=set()
unq=set()
for i in list2:
    count = 0
    for j in list2:
        if i==j:
            count += 1
    if count >1:
        dup.add(i)
    else: unq.add(i)
print(list(dup), "duplicates")
print(list(unq), "unique")

# bryte force - takes more time or more memory.
# for i in list2:

# dictionary method
