#sets are unordered collection of unique elements.
name = {10,10,20,30,40,50}
print(name) # Output: {10, 20, 30, 40, 50} - duplicates are removed

nums = {20,30,10}
nums.add(40)
print(nums)
a=sorted(nums)
print(a)

b = {10,20,30}
c = {30,40,50}

print(b|c) #printing 
print(b-c)
print(c-b)
print(b.union(c))
print(b.intersection(c))

# Symmetric difference: elements that are in either set, but not both.
print(b ^ c) # Output: {10, 20, 40, 50}
print(b.symmetric_difference(c)) # Same result

# Built-in functions used with sets
values = {10, 20, 30, 40}
print(len(values))                   # Number of elements
print(sorted(values))                # Sorted list of elements
print(min(values))
print(max(values))
print(sum(values))

# Set built-in methods
d = {10, 20, 30}
d.add(40)                         # Add one element
d.update([50, 60])                # Add multiple elements
print(d)

d.discard(60)                        # Remove an element without an error if absent
d.remove(50)                         # Remove an element and raise an error if absent
print(d)

removed = d.pop()                    # Remove and return an arbitrary element
print(removed)
d.clear()                            # Remove all elements
print(d)
