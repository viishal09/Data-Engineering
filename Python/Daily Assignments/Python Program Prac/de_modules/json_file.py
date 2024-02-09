# Import JSON module
"""
import json

# Define JSON string
jsonString = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'

# Convert JSON String to Python
student_details = json.loads(jsonString)

# Print Dictionary
print(jsonString)
print(student_details['name'])
print(student_details['course'])



import json

with open('sample2.json','r') as json_file:
    
    data = json.load(json_file)
    
    print(data['phoneNumbers'])
    print("\n",data)
    print("\n",data["lastName"])
    
    data1 = dict(data)
    #print(data)
    for key,val in data1.items():
        print(key,val)
    print(data['address']['state'])
    
    
import json

employee_details = '{"id":"09", "name": "Nitin", "department":"Finance"}'
employee_dict = json.loads(employee_details)

print(employee_dict)
print(employee_dict["id"])

for key,val in employee_dict.items():
    print(key)
    
    

    
# Python program to convert
# Python to JSON
import json

# Data to be written
# dictionary = {
#     "id": "04",
#     "name": "sunil",
#     "department": "HR"
# }

# Serializing json 
# json_object = json.dumps(dictionary, indent = 4)
# print(json_object)

    """

# Python program to write JSON
# to a file
import json

# Data to be written
dictionary ={
    "name" : "Vishal",
    "rollno" : 580,
    "cgpa" : 8.18,
    "phonenumber" : "9976770500"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
    
with open("sample.json") as outfile:
    read_file = json.load(outfile)
print(json.dumps(read_file,indent=4, sort_keys= True)) # sort_keys is used to sort the json array


