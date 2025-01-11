'''square = lambda x:x*x
print(square(5))'''
# 
'''l = [1,2,3,4,5]
square = lambda x:x*x
sqList = map(square,l)
print(list(sqList))
# Filter
def even(n):
    if (n%2==0):
        return True
    return False
onlyEven = filter(even,l)
print(list(onlyEven))
# Reduce
from functools import reduce
sum = lambda a,b:a+b
print(reduce(sum,l))'''


# 
'''name = input("ENter name")
marks = int(input("Enter marks"))
Contact = int(input("Enter contactNu: "))

s = "The name of the student is {},his marks are{} and phone nu: {}".format(name,marks,Contact)
    
print(s)'''
# 
'''table = [str(7*i) for i in range(1,11)]
s = "\n".join(table)
print(s)'''
# 
'''def divisioon5(n):
    if(n%5==0):
        return True
    return False

a = [1,2,34234,53,5543,223,4455]

f = list(filter(divisioon5,a))
print(f)'''
# 
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_World():
    return "<h1>Hello, World!</h1>"

app.run()