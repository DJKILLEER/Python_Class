# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23,
#     "Harry": 333
# }
# # print(marks,type(marks))
# # print(marks.values())
# marks.update({"Harry":99,"Killer":100})
# marks.clear()
# print(marks)

# s = {1,5,32,1,1,"killer"}
# e = set()
# print(s,type(s))
# s.add(566)
# print(s,type(s))
# s.remove(566)
# print(s,len(s))

# s1 = {1,45,6,78}
# s2 = {7,8,1,78}

# print(s1.union(s2))
# print(s1.intersection(s2))

# words = {
#     "chair": "kursi",
#     "building":"makan",
#     "haldi":"nipata",
#     "puspa":"chandan"
# }

# word = input("Enter word you want meaning of")

# print(words[word])
# s = set()
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))
# n = input("Enter number ")
# s.add(int(n))

# print(s)
dict = {}

name = input("Enter freinds name: ")
lang = input("Enter Language name: ")

dict.update({name: lang})
name = input("Enter freinds name: ")
lang = input("Enter Language name: ")

dict.update({name: lang})
name = input("Enter freinds name: ")
lang = input("Enter Language name: ")

dict.update({name: lang})
name = input("Enter freinds name: ")
lang = input("Enter Language name: ")

dict.update({name: lang})
print(dict)