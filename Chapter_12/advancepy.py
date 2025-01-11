
# walrus operator
'''if(n := len([1,2,3,4,5])>3):
    print(f"List is too long ({n} elements expected <=3)")
    '''
    # types
'''n : int = 5
name = str = "Harry"

def sum(a: int , b: int):
    return a+b

print(sum(2,3))'''
    # Match
'''def http_status(status):
     match status:
         case 200:
           return "Ok"
         case 404:
           return "Not found"
         case 500:
           return "Internal server error"      
         case _:
             return"Unknown status"
             
print(http_status(4040))     '''          


# exception
'''try:
    a = int(input("Enter a value: "))
    print(a)
    
except ValueError as v:
    print('Yuu')
    print(v)    
except Exception as e:
    print(e)   
else:    
    print("Thank you ")  '''  
    
#finally
'''try:
    a = int(input("Enter a value: "))
    print(a)
    
except ValueError as v:
    print('Yuu')
    print(v)    
except Exception as e:
    print(e)   
finally:    
    print("inside finally ") '''  
   
    #main
'''
def myfunc():
    print("Hello World")
    
myfunc()
print(__name__)'''
    
#
'''l = [1,2,3,4,5,6,7,8]
for i,item in enumerate(l):
     if i ==2 or i == 4 or i==6:
         print(item)'''
        #  
'''n = int(input("Enter a number: "))
table = [n*i for i in range(1,11)]
print(table)  '''      
# 
n = int(input("Enter numb: "))

table = [ n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(f"Table of {n}: {str(table)} \n")
         
         

