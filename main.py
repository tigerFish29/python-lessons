import platform

# comment 
print("this is python version {}".format(platform.python_version()))

# statements and expression => unit of evaluation 
# anything returning a value is an expression 
# x = y f() true x*y 
# statement is a line code in python by itself 
# print statement also an expression 
print("hello world")
# indententation 
def main():
    print("hello and welcome to this party")

#if __name__ == '__main__' : main()
x = 42
y = 73 

if x > y:
    print('x < y: x is {} and y is {}'.format(x,y))
    print('line 2')
    print('line 3')
    print('line 4')
print("something else")    

# elif like else if 
# loops a while and for loop 
# for loop iterates through a sequence 

words = [ "one3", "two", "three", "four", "five"]
n = 0 # set a variable 
while(n < 5):
    print(words[n])
    n += 1
# for loop 
for i in words:
    print(i) # each element of words 


# functions 
def function(n=1):
    print(n)

# none an absence of a value 
d = function(45)
print(d)

#objects and classes 
class Car:
    def drive(self):
        print("my car is driving =")

    def speed(self):
        print("my car is speeding ")

def main():
    mercedez = Car()
    mercedez.drive()
    mercedez.speed()


if __name__ == '__main__' : main()

# continue with python programming 
# python types class int 
# duck typing 
# class bool 
# single or double quotes 
# multi line string 
# strings are objects 
xyz = 34 
print(type(xyz))
# bool, type true or false 
# None the absence of a value 
# few things evaluate as false 
# sequence types 
x = [1,2,3,4,5,6,7,8]
for i in x:
    print(i)

# index starts at zero 
# can use the range operator 
# three parameters for the range operator // 
cities = {'one': 1, 'two': 2, 'three': 3}
for k,v in cities.items():
    print('k: {}, v: {}'.format(k,v))

# evertyhing is an object 
fruits = ('orange', 'mangoes', 'grapes')
print(type(fruits))
# class tuple 
# is operator 
# conditional 
if True:
    print("true")
elif False:
    print("elif true=")
else:
    print("Not working today")

# you can have many elifs 
# conditional operators 
# > > << or not is isNot 
# conditional expressions # tenary expressions operators 
hungry = 0 
x = "Feed the bear now!" if hungry else "Do not feed the bear"
print(x)

# needs to have the else clause 
# arithmetic operators 
# modular % without remainder //
# bitwise operators 
# operate on bits and numbers 
# comparison operators 
g = 43 
kz =  22
if g <= kz:
    print("comparison is true")
else:
    print("comparision is false")

# boolean operators
m = True
v = False 

if not v:
    print("expression is true")
else:
    print("expression is false")
# if y in x 
# operator precidence 
# operators have precedence 
secret = "babies"
pw = ""

while pw != secret:
    pw = input("What is the secret password?")
# uses a conditional expression to control the loop 


def main():
    x = ("meow", "grr", "purr", "hello", "world")
    kitten(*x)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
        else:
            print("meow")
    print("meow")

if __name__ == '__main__': main()
# all functions return a value even though its none 
# functional arguments 
# default value 
# inteeger not mutable 
# mutable objects 
# keyword arguments 
# function returns a value 
# empty return statement => none 
# genrator return a stream of values 
# range is a generator 
# raise a type error 
# decorator returns warapper function 
# everything is an object 
# # everything is an object 
# functions define scope 
# decorator 

def f1():
    def f2():
        print("this is the f2 template")
    return f2

def f3():
    print('this is f3')

# lists and tuples 
# tuples are immutable 
def mains():
    game = ['rock','paper','spock']

# join method on the array list method 
# tuples cannot be changed 
# tuples favoured 
# dictionary hashed arrays 
# similar to objects in other languages 
# key - value pair 
# dictionary constructor to create a dict 
# keys must be immutable 
# sets do not allow for duplicates 
# lists are not ordered 
# list comprehension like the list of lists 
fruitz = ["apple","banana","cherry","kiwi","mangoi"]
newFruits = [] 

for x in fruitz:
    if "a" in x:
        newFruits.append(x)


print(newFruits)
# example above without list comprehension 

# example with list comprehension 
new_fruits = [x for x in fruitz if "a" in x]
print(new_fruits)

# the syntax 
# new list [expression for item in iterable if condition == true]
# mixed structures 
# possible to store anything in a data structure 
# everything is an object 
# can create any structured data 
# classes 

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

# object methods with self 
    def myFunc(self):
        print("Hello my name is " + self.firstName)
person1 = Person("Brian", "mulenga", 28)
print(person1.firstName)
print(person1.age)   
# getters and setters in classes 
# arguments can have default values s
# constructor 
# constructor initialises the object 
# inheritance 

class Student(Person):

    def __init__(self, studentNumber, course, university):
        self.studentNumber = studentNumber
        self.course = course
        self.university = university

        super().__init__(firstName="kevin",lastName="charles", age=22)
    
txy = Student(78956, "Medicine", "University of Ottawa")
print(txy.age)
print(txy.myFunc())

# everything is an object in python 
# iterator class that provides iteration 
