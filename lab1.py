# COMMENTS IN PYTHON
x=1
#the initial value of x is 1
if x>0:
    print("These are two comments") # Print a string

# INPUT/OUTPUT
txt=input("Type something to test this out:")
print(txt)

#Multiple statement on a single line
print("statement1")
print("statement2")
#You can write above code as
print("statement1");print("statement2")

#Single space indentation
x=1
if x>0:
 print("This statement has a single space indentation")
 print("This statement has a single spce indentation")

 #Single Tab indentation
 x=1
 if x>0:
    print("This statement has a single tab indentation")
    print("This statement has a single tab indentation")

#Single Space and Tab indentation
x=1
if x>0:
     print("This statement has a single space+tab indentation")
     print("This statement has a single space+tab indentation")

#Data types and Type casting
a=1324
type(a)
print(type(a))
b=(-3453)
type(b)
print(type(b))
c=0
type(c)
print(type(c))
h=1.35
type(h)
print(type(h))
i=(-3.87)
type(i)
print(type(i))
v='t'
type(v)
print(type(v))

#complex numbers
x=complex(1,8)
type(x)
print(x)
print(type(x))

z=1+2j
type(z)
print(type(z))

l=2+3J
type(l)
print(type(l))

#Boolean 
x=True
type(x)
print(type(x))

y=False
type(type(y))
print(type(y))

#Strings
str1="day's"
print(str1)

str2='day"s'
print(str2)

#Special characters in string
print("This is a backlash(\\) mark.")
print("This is a tab \t key.")
print("These are \'single quotes\'.")
print("These are \"double quotes\".")
print("This ia a new\n line.")

#String indices and accessing string elements
string="PYTHON TUTORIAL"
print(string[0])
print(string[10])
print(string[-15])
print(string[10])
print(string[-12])
print(string[14])

#Lists
my_list1=[5,12,8,17]
print(my_list1)
my_list2=['red','yellow','purple','blue']
print(my_list2)
my_list3=['red',12,11.78]
print(my_list3)

#List indices
my_list1=['red','brown','yellow']
print(my_list1[0])
print(my_list1[-2])

#List Slices
colour_list=["red","blue","green","black"]
print(colour_list[0:2])
print(colour_list[1:2])
print(colour_list[1:-2])
print(colour_list[:])
print(colour_list[:2])

