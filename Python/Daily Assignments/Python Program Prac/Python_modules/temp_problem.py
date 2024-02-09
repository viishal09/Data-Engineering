import temp

print(round(temp.to_centigrade(12),3))

print(round(temp.to_fahrenheit(54),3))




# fetching an object of the module
print(temp.FREEZING_F)
print(temp.FREEZING_C)


# importing the to_fahrenheit() method
from temp import to_fahrenheit

# using the imported method
print(to_fahrenheit(20))

# importing the FREEZING_C object
from temp import FREEZING_C

# printing the imported variable
print(FREEZING_C)