student = {
    "id": 1,
    "name": "tharun",
    "course": "python",
    "cgpa": 91.54,
    "address": "hyderabad" 
}

print(student["id"])
print(student["name"])
print(student["course"])
print(student["cgpa"])
print(student["address"])

print(student.get("salary"))  #output : none as there is no key called salary

#adding a new key
#dict_name["new_key"]="value"

student["number"] = "0123456789"
print(student)

#updating the value
student["number"] = "9874563210"
print(student)

print(student.keys())

#items()

for key, value in student.items():
    print(key,value)

print(student.items())

#updating the dictionary
student.update({
    "name": "abhilash",
    "number": "9876543210"
})

c = student.pop("number")
print(student)
print(c)

# student.clear()
# print(student)

print(len(student)) #printing the length of the dictionary (no.of keys)

print(max(student))

print(sorted(student)) #sorts the dictionary in alphabetical order