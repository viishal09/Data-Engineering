myset = {"abhi", "david","sunil", "ram", "aditya"}




print("before adding :",myset)

# add method

myset.add("abhishek")
myset.add(10)
print("after adding :",myset)

# remove method

print("before",myset)
myset.remove("abhi")

print("set after remove method",myset)



# discard method
print("before", myset)
myset.discard("ram")
print("after discard :",myset)



# pop method
print("before", myset)
myset.pop()
print("after",myset)



# clear method 

print("before", myset)
myset.clear()
print("after",myset)




# del method 

print("before", myset)
del myset
print("after",myset)



# union method

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union()
# function
population = people.union(vampires)

print("Union using union() function : ")
print(population)



people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

population = people|dracula

print("\nUnion using '|' operator")
print(population)


# intersection 

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}
set3 = set1.intersection(set2)
print(set3)


# difference 

set4 = set1.difference(set2)
print(set4)




# update
myset2 = {"amitab"}
print("before",myset)
myset.update(myset2)
print("after",myset)