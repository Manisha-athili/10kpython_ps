# Q1) A biometric security system needs to generate a secure PIN from a user's fingerprint data. Each scanned fingerprint is converted into a unique number, and the system extracts the smallest prime digit from this number to enhance security checks. If no prime digits exist, it alerts the user.
# Your task is to write a program that finds the smallest prime digit (2, 3, 5, or 7) in a given number.

num = int(input("Enter you pin:")) #57432
temp = num
def check_small_prime(num):
    prime_list = [2,3,5,7]
    small_prime = -1
    while num>0:
        digit = num%10 #last digit of the num or input
        num=num//10 #num leaving last digt removing last digit
        if digit in prime_list:
            if small_prime==-1 or small_prime>digit:
                small_prime=digit
                                
    if small_prime != -1:
        return small_prime
    else:
        return f"{small_prime} not found prime digit"
print(check_small_prime(temp))
