# Python program to illustrate 
# while loop 
count = 0 
while (count < 3): 
    count = count + 1 
    print("Hello Geek")

# Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
 print(i)

# Python program to illustrate 
# Iterating by index 
list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
 print( list[index] )

 # Iterating over a String 
print("\nString Iteration") 
s = "Geeks" 
for i in s : 
    print(i)

    # Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
 if letter == 'e' or letter == 's': 
    continue 
 print ('Current Letter :', letter) 
 # break the loop as soon it sees 'e' 
# or 's'
print("this program shows the break statement ")
for letter in 'geeksforgeeks': 
   if letter == 'e' or letter == 's': 
        break 
print ('Current Letter :', letter)

#creating a function
def my_function(): 
  print("Hello from a function")

my_function();  

#parameters
def my_function(fname): 
  print(fname + " Refsnes") 
my_function("Email") 
my_function("Tobias") 
my_function("Linus")

#default parameter
def my_function(country = "Norway"): print("I am from " + country) 
my_function("Sweden")  
my_function("India")  
my_function()  
my_function("Brazil") 

#passing a list as a parameter
def my_function(food): 
 for x in food: 
   print(x) 
fruits = ["apple", "banana", "cherry"] 
my_function(fruits);

#returning values
def my_function(x): 
  return 5 * x 
print(my_function(3)) 
print(my_function(5)) 
print(my_function(9))

#Keyword Arguments
def my_function(child3, child2, child1): 
  print("The youngest child is " + child3) 
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#creating a class
class MyClass: x = 5
p1 = MyClass() 
print(p1.x) 

#object method
print("Object function")
class Person:
  def __init__ (self, name, age): 
   self.name = name
   self.age = age

  def myfunc(self):
   print("Hello my name is " + self.name)

p1 = Person("John", 36) 
p1.myfunc()

