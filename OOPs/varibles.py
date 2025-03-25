# types of varibles : 
# 01 instance varibles
# 02 class or static varibles


# 01 instance varibles : varibles that belongs to a particular instance of a class

# 02 Class Ststic varibles : are the static = values are same for all obj
        #   these varibles can be access by classname and objects also

class HumanBeing():
    speices = "homosepians"
    def self_intro(self):
        print(f"Hi, I am Human, I dont know my name")
        
    def __init__(self, name1,age1,batchNo):
        self.name = name1
        self.age = age1
        self.batch = batchNo
        print("im constructor")


human1 = HumanBeing("girly1","24","27r")
human2 = HumanBeing("girly2","24","27r")
human3 = HumanBeing("girly3","24","27r")
human4 = HumanBeing("girly4","24","27r")

print(human1.name) #instance
print(human1.age)
# print(HumanBeing.name)  error instance varible by class 
print(HumanBeing.speices) # static varible by class
print(human1.speices)  #  varible by instance

