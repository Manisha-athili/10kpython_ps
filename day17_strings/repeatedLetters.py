
str1 = "takeuforward"
inp ="forward"
flag = False

for i in range(len(str1)):
    for j in range(i+1,len(str1)+1):
        # print(str1[i:j])
        if str1[i:j] == inp:
            print(i)
            flag = True
            break
    if flag == True:
        break

# for i in str1:
#     if len(inp)== str1[]

for i in range(len(str1) - len(inp) + 1):   # 12 - 7=5 +1 = 6
    if str1[i:i+len(inp)] == inp:  # 
        print(i)

#  i = 0  ==>  0:0+6 == inp = t 
#  i = 1  ==> 1: 1+6 == 1:7 = a
#  i = 2 ==>  2: 2+6 == 2:8 = k
#  i = 3 ==> 3: 3+6 == 3:9  = e
#  i = 4 ==> 4: 4+6 == 4:10 = u
#  i = 5 ==> 5: 5+6 == 5:11 = f  checks from here 









    