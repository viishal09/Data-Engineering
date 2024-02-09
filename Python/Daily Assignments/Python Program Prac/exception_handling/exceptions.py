

#ZeroDivisionError

num = int(input())
try:
    res = num/0
except ZeroDivisionError :
    print("Division is not possible with zero")
finally:
    print("Finally is executed")
  
   
   
# Type Error
x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")
    

     
# Name Error

try:
    print(a)
except NameError:
    print("The exception raised is : ",NameError) 
        
    
try: 
    raise NameError("Hi there")
except NameError:
    print ("An exception")
    raise

