str1 = "Destop"

def reverse(str1):
    if len(str1) <= 1:
        return str1
    return str1[-1] + reverse(str1[0:-1])
print(reverse(str1))
