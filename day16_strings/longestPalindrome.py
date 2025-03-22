
str1 = "abccbc"
list1 = []
for start1 in range(len(str1)):
    for end1 in range(start1+1,len(str1)+1):
        print(str1[start1:end1])
        list1.append(str1[start1:end1])
print(list1)


# def is_polindrome(str1):
#     str2 = ""
#     for i in range(len(str1)):




# is_polindrome(str1[start1:end1])