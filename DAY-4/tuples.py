#tuple-tuple is a collection which is ordered and unchangeable. 
# In Python tuples are written with round brackets '()'.
#tuple is immutable, meaning that you cannot change, add, or remove items once the tuple is created.

nums=(1, 2, 3, 4, 5) #creating a tuple
print(nums[0:3]) #printing the tuple from index 0 to 2
print(nums[2:4]) #printing the tuple from index 2 to 3

nums1=(1, 2, 3, 4, 5) #creating a tuple
nums2=(10,) #creating a tuple with one element
print(nums1+nums2) #printing the concatenation of two tuples

print(nums1*3) #printing the tuple nums1 three times

print(len(nums1)) #printing the length of the tuple nums1

nums3=(3, 1, 4, 2, 5) #creating a tuple
print(sorted(nums3)) #printing the sorted tuple
print(sorted(nums3, reverse=True)) #printing the sorted tuple in descending order

nums4=(4,5,2,1,2,4,2,1)
print(nums4.count(2)) #printing the count of 2 in the tuple nums4
print(nums4.index(2)) #printing the index of the first occurrence of 2 in the tuple nums4

#converting a tuple to a list
nums5=(1, 2, 3, 4, 5) #creating a tuple
nums_list=list(nums5) #converting the tuple to a list
nums_list.append(6) #adding an element to the list
print(nums_list) #printing the list after adding an element

#converting a list to a tuple
nums_list1=[1, 2, 3, 4, 5] #creating a list
nums_tuple=tuple(nums_list1) #converting the list to a tuple
print(nums_tuple) #printing the tuple after converting from list



