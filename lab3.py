'''#program 1

for i in range(1500,2700):
   if i%7==0 and i%5==0:
      print(i);
#program to convert temperature
temp=float(input("Give temperature in celcius:"))   
f=(temp*9/5)+32  
print(temp," in fahrenheit is ",f)

#program to convert temperature
temp2=float(input("Give temperature in celcius:"))   
c=(temp2-32)*5/9
print(temp2," in celsius is ",int(c))

#random number
import random
num=random.randint(0,9)   
n=int(input("enter your guess "))
while n!=num:
   n=int(input("again enter your guess "))
print("Well guessed") 

#nested loop to print a pattern
for i in range(1,6):
   for j in range(1,i+1):
      print("*",end=" ")
   print(" ")   
for i in range(1,5):
   for j in range(4,i-1,-1):
         print("*",end=" ")   
   print(" ")      

#2nd way
for i in range(1,6):
   print("*"*i)
for j in range(4,0,-1):  
   print("*"*j)
  

#program 5
text=input("Enter a word: ")
reversed_string=text[::-1]
print(reversed_string)

# program 6
list=[1,2,3,4,5,6,7,8,9]
j=0
k=0
for i in list:
    if i%2==0:
        j=j+1
    else:
        k=k+1   

print("Number of Even numbers: ",j)        
print("Number of Even numbers: ",k)  

#program 7
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print("Data: ",i," Type: ",type(i))

#program 8
for i in range(0,7):
    if i==3 or i==6:
       continue
    print(i)  

#program 9
start=0
end=50
b=1
while  start<=end:
    print(start,end=" ")
    start,b=b,start+b

#program 10
for i in range(1,51):
    if i%3==0 and i%5==0:
       print("FizzBuzz")  
    elif i%3==0:
      print("Fizz")
    elif i%5==0:
      print("Buzz")
    else :
       print(i)  

#program 11
m=int(input(" Enter Row value"))
n=int(input(" Enter col Value"))
multi_list=[[0 for col in range(n)]for row in range(m)]
for row in range(m):
    for col in range(n):
        multi_list[row][col]=row*col

print(multi_list) 

#program 12
lines=[]
while True:
    l=input()
    if l:
        lines.append(l.lower())
    else:
        break    

for l in lines:
    print(l)


#2nd method
binary_num=input()
split_input=binary_num.split(',')
num=[]
for x in split_input:
    num.append(x)
print(num)   

#progarm 13
str=input()
count=0
l=0
for i in str:
    if i.isdigit():
        count=count+1
    elif i.isalpha():
        l=l+1
    else:
        pass    
print("Letters: ",l) 
print("Digits: ",count)   '''

# program 15
import re
p = input("Input your password")

x = True

while x:  
    
    if (len(p) < 6 or len(p) > 12):
        break
    
    elif not re.search("[a-z]", p):
        break
    
    elif not re.search("[0-9]", p):
        break
    
    elif not re.search("[A-Z]", p):
        break

    elif not re.search("[$#@]", p):
        break

    elif re.search("\s", p):
        break

    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")