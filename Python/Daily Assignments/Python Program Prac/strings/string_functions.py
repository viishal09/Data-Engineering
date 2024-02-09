
# input from users 
inp1 = "mY name is abhi"
inp2 = "MY name is ram"

# Convert case using capitalize() 
capitalized_string = inp1.capitalize() 
print("Sentence 1 output -> ", capitalized_string) 
capitalized_string2 = inp2.capitalize() 
print("Sentence 2 output -> ", capitalized_string2) 



#lower()

s1 = "ABHI"
s2 = s1.lower()
print(s2)


#upper() 

s3 = "abhiram"
s4 = s3.upper()
print(s4)


#isalpha()
s = "abhi"
for ch in s:
    if ch.isalpha() == True:
        print("current char is :",ch)


txt = "Company12"

x = txt.isalnum()

print(x)
  

txt = "hexaware"

x = txt.count("e")

print(x)



txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)



txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)