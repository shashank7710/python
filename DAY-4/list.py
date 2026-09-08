#list concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# using + operator
result=list1+list2
print(result) #printing concatenated list
print(list1*3) #printing list1 three times

#built-in functions
a = [1, 2, 3, 4, 5]

#max() function returns the largest value in the list
print(max(a)) #printing maximum value in list

#min() function returns the smallest value in the list
print(min(a)) #printing minimum value in list

#sum() function returns the sum of all values in the list
print(sum(a)) #printing sum of all values in list

#len() function returns the number of elements in the list
print(len(a)) #printing length of list

#sorted() function returns a new sorted list from the elements of any iterable
b = [3, 1, 4, 2, 5]
print(sorted(b)) #printing sorted list
print(sorted(b, reverse=True)) #printing sorted list in descending order

#list methods
c = [1, 2, 3, 4, 5]

#append() method adds an element to the end of the list
c.append(6)
print(c) #printing list after appending an element

#extend() method adds all elements of an iterable to the end of the list
c.extend([8,9,10]) #extending list with another list
print(c) #printing list after extending with another list

#remove() method removes the first occurrence of an element from the list 
c.remove(3) #removing 3 from the list
print(c) #printing list after removing an element

#insert() method adds an element at a specific index in the list
c.insert(2,3) #inserting 3 at index 2
print(c) #printing list after inserting an element

#pop() method removes and returns the element at a specific index in the list
c.pop(2) #removing element at index 2
print(c) #printing list after popping an element
print(c.pop(0)) #printing the popped element
print(c) #printing list after popping an element

#index() method returns the index of the first occurrence of an element in the list
print(c.index(8)) #printing index of 8 in the list

d=[10,20,30,40,30]
#count() method returns the number of occurrences of an element in the list
print(d.count(30)) #printing count of 30 in the list

#sort() method sorts the elements of the list in ascending order
e=d.sort()
print(e) #printing None, as sort() returns None
print(d) #printing sorted list

f=sorted(d) #sorting list in ascending order
print(f) #printing sorted list
#sorted creates a new list, while sort() modifies the original list in place.

#reverse() method reverses the elements of the list in place
d.reverse()
print(d) #printing reversed list

#clear() method removes all elements from the list
d.clear()
print(d) #printing empty list after clearing all elements

#finding maximum and minimum values in a list without using built-in functions

g = [1, 2, 3, 4, 5]
max_val = g[0]
for i in g:
    if i>max_val:
        max_val = i
print(max_val) #printing maximum value in the list

min_val = g[0]
for i in g:
    if i<min_val:
        min_val = i
print(min_val) #printing minimum value in the list

 