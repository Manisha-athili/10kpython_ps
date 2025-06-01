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


# day21 26-march
# types of methods: 3
# instance methods : atleast one instance varible
# static method: no variable
# class methods : atlest one class or static verible ...(in other lang static and class is same but not in py)


# class shape:
#     total_count = 0
#     def __init__(self,sides):
#         self.side = sides
#         print("shape created")
#         total_count +=1
#     def cal_area(self):
#         print("area of shape is",self.side**2)

#     def change_side(self, new_side):
#         self.side = new_side
#         print("num of sides")

#     @classmethod
#     def reset_total_count(cla):
#         cla.total_count=0
#         print("count set to zero")

#     @staticmethod
#     def info():
#         print("we have 2 varibles and 3 methods")


# poly1 = shape(2)
# poly1 = shape(1)
# poly1 = shape(3)
# poly1 = shape(8)

# / 4 main concepts of OOPs - I APE

# Inheritance : childe (or sub class) inheriting the properties from parent class(super class)
#  single 
# multiple inheritance
# multiLevel inheritance

# 27 march day22

#  multiLevel inheritance : childe (or sub class) inheriting the properties from two or more classes
class User():
    pass
class teacher():
    pass
class student():
    pass


# multiple childe (or sub class) inheriting the properties from two or more classes

class Lion():
    def roar(self):
        print("Lion is Roaring")
class Tiger():
    def hunt(self):
        print("tiger is hunting")
class Liger(Lion,Tiger):
    pass

obj = Liger()
obj.roar()
# print(obj.roar())

print("28-03-2025")
# 28/03

# Encapsulation :  is a process of hiding data for safety and pravicy perpous using setters and getters 
# Access specifiers : private, public , protected
# public - no restrictions - everywhere can accessed (by default)
# private - only within the class defination only (to use : __ double underscore : before the varible name)
#  this can be modified by using getters and setters
# protected - access to within the class and its childern (_) single underscore : before the varible)
# In only python we can access protected out side the class also....
class HumanBeing:
    def __init__(self,name,phn_number,dob):
        self.__name=name  # private 
        self.__phn_num = phn_number
        self.dob = dob
        print("human obj")
    def get_phn_num(self):
        return self.__phn_num
    def set_phn_num(self,new_num):
        self.__phn_num = new_num
        print("Phone number has been updated")
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
        print("Name has been updated")

hm1= HumanBeing('manisha',9065432,2345)
print(hm1)
print(hm1.name)
hm1.set_name('hello')
print(hm1.get_name)


# Abstraction : a process of hiding implimentation details.
# abstract classes : no logic - just the skeleton of the class
#  any class with abstract method is called abstract class
# Abstract Method : without any defination
# all the methods in the Abstract should be implementes
#we cant create obj for class

from abc import ABC, abstractmethod

# Abstract Class
class ATM(ABC):

    @abstractmethod
    def withdrawl(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    # this is the skeleton only

# actual code
class SBI_atm(ATM):
    def withdrawl(self):
        print("sbi withdrawl")
    
    def deposit(self):
        print("deposit")

# create obj to call class
sb_atm = SBI_atm()








