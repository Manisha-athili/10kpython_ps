arr1 = [568,89,112,88,571]
inp = 88

def check(arr1,inp):
    for i in arr1:
        if i == inp:
            return True
    return False
print(check(arr1,inp))

# tc : O(n) linear time complixity
# sc : O(1) constant space complexity



