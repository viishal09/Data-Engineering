
var = {"Hexaware", "for"}
print(type(var))

print(len(var))


# Accessing elements of set using for loop 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
    
   
# typecasting list to set
myset = set(["a", "b", "c"])
print(myset)


 
normal_set = set(["a", "b","c"])

frozen_set = frozenset(normal_set)

print(frozen_set)
frozen_set.add("e")
print(frozen_set)
# we cannot add items to frozen set


normal_set = {"a", "b","c"}
for i in range(1,6) :
    normal_set.add(i)
print(normal_set)



