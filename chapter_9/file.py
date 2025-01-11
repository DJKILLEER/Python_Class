'''
f = open("file.txt","r")
data = f.read()
print(data)
f.close()'''
'''
 st = "Here are started "

 f = open("files","w")
 f.write(st)
 f.close()
'''

"""f = open("file.txt")
lines = f.readlines()
print(lines,type(lines))
f.close()"""

# f = open("file.txt")
'''line1 = f.readline()
print(line1,type(line1))
line2 = f.readline()
print(line2,type(line2))
line3 = f.readline()
print(line3,type(line3))
line4 = f.readline()
print(line4,type(line4))
line5 = f.readline()
print(line5,type(line5))'''

'''line = f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()'''

# f = open("file.txt")
# print(f.read())
# f.close()

# the same can be written using with statement like: -
# with open("file.txt") as f:
#     print(f.read())
    # you dont have to close file in this 
    
    # practice set
'''f = open("poem.txt")
content = f.read()
if("yr" in content):
    print("present")
 
else:
    print("Absent")    
f.close()    '''
'''import random
def game():
    print("You are playing the game")
    score = random.randint(1,62)
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
               
    print(f"Your scoe:{score}")
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
        
        
    return score

game()'''
#table
'''def genrateTable(n):
        table=""
        for i in range(1,11):
            table += f"{n} X {i} = {n*i}\n"
            
        with open(f"tables/table_{n}.txt","w") as f:
            f.write(table)
        
        
                
for i in range(2,21):
    genrateTable(i)   ''' 
    
    
    