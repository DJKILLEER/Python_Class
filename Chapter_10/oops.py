'''class Employee:
    name = "Killer"
    lang = "py"
    salary = 12000000'''
    
'''    def __init__(self,name,salary,lang):
        self.name = name
        self.salary = salary
        self.lang = lang
        print("Created object")
    
    def getInfo(self):
        print(f"your language is {self.lang}, your salry is {self.salary}")
        
    def greet(self):
        print(f"goodmorning {self.name}")    
        
        
killer = Employee("Killer",120000,"JS")
print(killer.name,killer.salary)

aarya = Employee("aarya",9000,"Python")        
print(aarya.name,aarya.salary)'''
    
# killer = Employee()
# killer.name = "Killer"
# print(killer.name)
# killer.getInfo()
# killer.greet()
# aarya = Employee()
# aarya.name = "aarya"
# print("\n")
# print(aarya.name)
# aarya.getInfo()
# aarya.greet()

#1
'''class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        

p = Programmer("Killer",12000,9090)      
print(p.name,p.salary,p.pin,p.company)  
a = Programmer("aarya",1000,9090)      
print(a.name,a.salary,a.pin,a.company)  '''
#2
'''class calaculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"square is {self.n*self.n}")    
    def cube(self):
        print(f"square is {self.n*self.n*self.n}")    
    def sqroot(self):
        print(f"square is {self.n**1/2}")    
        
a = calaculator(4)     
a.square() 
a.cube()
a.sqroot()'''
#3
class Demo:
    a = 4 #instance attribute
o = Demo()
o.a = 0 # class atrribute
print(Demo.a)   #answer 4 