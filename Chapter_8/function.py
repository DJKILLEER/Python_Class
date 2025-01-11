
# def avg():
#     a = int(input("Enter your numb: "))
#     b = int(input("Enter your numb: "))
#     c = int(input("Enter your numb: "))

#     average = (a+b+c)/3
#     print(average)

# avg()   

# def goodDay(name):
#     print(f"Good day {name}")

# goodDay("killer")    
# goodDay("Rohit")    
# goodDay("Kolamṇ")    

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n*factorial(n-1)

# n = int(input("Enter adigit"))
# print(f"factorial of numb: {n} is",factorial(n))

# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
# print(greatest(2,33,4))

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1)+n

# print(sum(4))

def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(3)    