#Why Oops:
# disadvantages of Procedural programmes?

# class is the umbrella term where the behaviour(methods , varibles) of obj is given.
#  obj is actuall entity, instance of class 


class HumanBeing():
    def self_intro(self):
        print(f"Hi, I am Human, I dont know my name")
    pass

human1 = HumanBeing()
human2 = HumanBeing()
human4 = HumanBeing()

print(human1)
print(human2)
print(type(human1))


# calling method 

human1.self_intro()
human4.self_intro()

# varible and their use:

# first method to ....

human1.name = "manisha"
human1.batch = "29r"
human2.name = "hello"
human2.batch = "29r"

print(human1.name)
print(human2.batch)
# print(human3.name) error


# 2nd method using CONSTRUCTOR :

# CONSTRUCTOR: it is a method which is called when an instance of the class is created.
#  parameter name can be anything


class HumanBeing():
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

# accesing values: 

print(human1.name)
print(human2.name)
print(human3.name)
# self : object is stored automatically in self my compliler.
# self is passed as parameter but no need to send as argument.

# types of varibles : 
# 01 instance varibles
# 02 class or static varibles

