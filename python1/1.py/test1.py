# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# a = 50
# b = 78
# c = 45
# z = "ali is {} and bezi iz {} and beh is {}"
# z = z.format(a,b,c,)
# print(z)

# txt = "We are the \\\ so-called \"Vikings\" from the north."
# print(txt)

# txt = "Hello\f World!"
# print(txt)

# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple", 7, 24)

# print(x)

# x = "ali"
# print(x.center(20,'/'))

# x = 1.2

# print(isinstance(x,int))
# print(int(x))


# x = 34

# x >>= 2

# print(x)

# thislist = ["apple", "banana", "cherry"]

# thislist[1:1] = ["blackcurrant", "watermelon"]

# thislist.insert(3,'salam')
# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# thislist.extend("orange",'ali')

# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# thislist.clear()

# print(thislist)

# thislist = ["apple", "banana", "cherry"]

# for x in thislist :
#     print(x)

# thislist = ["apple", "banana", "cherry"]
# thislist.sort(reverse=False)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[-2:]
# print(mylist)


# import os
# os.remove("ali.txt")



# thistuple = ("apple", "banana", "cherry") # note the double round-brackets
# print(thistuple)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# thisset.add("orange")

# print(thisset)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 & set2
# print(set3)

# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]

# fruits.update(more_fruits)

# print(fruits)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x, y in thisdict.items():
#   t = "{}:{}"
#   print(t.format(x,y))

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car['brand']

# print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# x = car.setdefault("color", "White")

# print(x)
# print(car)

# def my_function(kids):
#       print("The youngest child is " + kids)

# my_function("Emil")

# def my_function(x):
#       print(x)

# my_function()

# class Person:
#       def __init__(self,fname, lname):
#             self.firstname = fname
#             self.lastname = lname

#       def printname(self):
#             print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")

# x.printname()


# class Person:
#       def __init__(self, fname, lname):
#             self.firstname = fname
#             self.lastname = lname

#       def printname(abc):
#             print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Person:
#       def __init__(self, fname, lname):
#             self.firstname = fname
#             self.lastname = lname

#       def printname(self):
#             print(self.firstname, self.lastname)

# class Student(Person):
#       def __init__(self, fname, lname):
#             Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()

# class MyNumbers:
#       def __iter__(self):
#             self.a = 1
#             return self

#       def __next__(self):
#             if self.a <= 20:
#                   x = self.a
#                   self.a += 1
#                   return x
#             else:
#                   raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myclass:
#   print(x)

# def myfunc():
      
#       x = 300

# myfunc()

# print(x)

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

