
#1
'''class TwoDvector:
    def __init__(self,i,j):
        self.i = 1
        self.j = j
        
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j") 
           
class ThreeDVector(TwoDvector):
    def __init__(self,i,j,k):
       super().__init__(i,j)
       self.k = k
    
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")    
       
a = TwoDvector(1,2)
a.show() 
b = ThreeDVector(5,2,3)       
b.show()'''     

#2
'''class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!")
        
d = Dog()
d.bark()'''
  
#3
'''class Empolyee:
    salary = 234
    increment = 20
    @property
    def salaryAfterIncre(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncre.setter
    def salaryAfterIncre(self,salary):
        self.increment = ((salary/self.salary) -1) * 100

e = Empolyee()
# print(e.salaryAfterIncre)
e.salaryAfterIncre = 280.8
print(e.increment)'''
    
#4
'''class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
        
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i) 
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
 
c1 = Complex(1,2)       
c2 = Complex(3,4)       
print(c1+c2)'''

#5
class Vector:
    def __init__(self,l):
        self.l = l
        
    def __len__(self):
        return len(self.l) 
    
vl = Vector([1,2,3])
print(len(vl))       