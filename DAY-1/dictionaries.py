#dictionary - unordered collection of key-value pairs => {key: value}
student = {"name": "ram ",
           "age": 20,
           "grade": "A"}
# Accessing values using keys
print(student["name"])  # Output: ram 
print(student["age"])   # Output: 20
print(student["grade"]) # Output: A

print(student.keys())  # Output: dict_keys(['name', 'age', 'grade'])

#type conversion - changing one data type to another 

a = "100"
b = int(a)
print(b)  # Output: 100

a=100
b=float(a)
print(b)  # Output: 100.0

# #int()
# #float()
# #str()
# bool()
# list()
# tuple()
# set()