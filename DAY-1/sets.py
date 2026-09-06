#set - unordered collection of unique elements => {}

seen = {1, 2, 3, 4, 5}
print(seen)  # Output: {1, 2, 3, 4, 5}

numbers = {1, 2, 2, 3, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4} - duplicates are removed

#adding elements to a set

fruits = {"apple", "banana", "mango"}
fruits.add("orange")
print(fruits) #output: {'banana', 'mango', 'orange', 'apple'}

#adding multiple elements to a set

fruits = {"apple", "banana"}
fruits.update(["mango", "orange", "grapes"])
print(fruits)

#removing elements from a set
a = {1, 2, 3, 4, 5}
a.remove(3)  # removes 3 from the set
print(a)  # Output: {1, 2, 4, 5}
