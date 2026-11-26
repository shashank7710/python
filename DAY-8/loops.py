#loops - doing the same thing over and over again
# for loop - when we know how many times we want to repeat the code
# while loop - when we don't know how many times we want to repeat the code

# for loop using index
# for i in range(1, 11):
#     print("Hello World")

# nums = [10,20,30,40,50]
# for i in range(0,5):
#     print(nums[i])

#by using values
# for num in nums:
#     print(num)

#while loop
# a = 1
# while a <= 5:
#     print(a)
#     a+=1

#print even numbers from 1 to 10
#for loop
# for i in range(1,11):
#     if i%2==0:
#         print(i)


#while loop
# i = 1
# while i<=10:
#     if(i%2==0):
#         print(i)
#     i+=1

#printing reverse numbers

# for i in range(10,0,-1):
#     print(i)

#while loop

# i=10
# while i>=1:
#     print(i)
#     i-=1

#sum of 1 to 10 numbers

# total=0
# for i in range(1,11):
#     total+=i
# print(total)

#multipication table

# table = int(input("enter a number: "))
# for i in range(1,11):
#     print(f'{table}*1 = {table * i}')

#finding largest number without using max()

nums = [10,20,40,30,50]
largest=nums[0]
# for num in nums:
#     if num>largest:
#         largest = num
# print(largest)

#using while loop
i = 1
while i < len(nums):
    if nums[i]>largest:
        largest = nums[i]
    i+=1
print(largest)
