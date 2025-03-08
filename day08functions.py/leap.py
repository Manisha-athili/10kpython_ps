year = int(input("Enter year : "))
def Check_leapyear(year):
    return True if(year%4==0 and year%100!=0) or year%400 == 0 else False
print(Check_leapyear(year))