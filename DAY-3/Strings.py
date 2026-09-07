#string slicing 
#variable_name[start:stop]
word = "python"
print(word[0:2])  # prints the first two characters
print(word[2:4])  # prints the third and fourth characters
print(word[4:6])  # prints the fifth and sixth characters
#variable_name[start:stop:step]
print(word[0:6:2])  # prints every second character from the first to the sixth

#reversing a string
print(word[::-1])  # prints the string in reverse order
print(word[5:0:-1])  # prints the string in reverse order from the last character to the second character
print(word[::-2]) # prints every second character in reverse order
print(word[0::]) # prints the entire string from the first character to the last character   

#concatenation of strings - joining two or more strings together
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)  # prints "Hello World"

age = 25
print("I am " + str(age) + " years old.")  # prints "I am 25 years old."

#membership operators - in and not in
sentence = "Python is a powerful programming language."
print("Python" in sentence)  # prints True
print("Java" in sentence)  # prints False
print("Java" not in sentence)  # prints True

#methods of strings: upper() - converts the string to uppercase, 
# lower() - converts the string to lowercase, 
# capitalize() - capitalizes the first character of the string, 
# title() - capitalizes the first character of each word in the string, 
# strip() - removes leading and trailing whitespace from the string

python_string = "python programming"
print(python_string.upper())  # prints "PYTHON PROGRAMMING"
print(python_string.lower())  # prints "python programming"
print(python_string.capitalize())  # prints "Python programming" only the first character of the string is capitalized.
print(python_string.title())  # prints "Python Programming" each word in the string is capitalized.

a = "     python is a programming language.     "
print(a.strip()) # removes leading and trailing whitespace from the string
print(a.lstrip()) # removes leading whitespace from the string
print(a.rstrip()) # removes trailing whitespace from the string
a=a.strip() # removes leading and trailing whitespace from the string and assigns it to the variable a
print(a.replace("python", "java")) # replaces "python" with "java" in the string
print(a.count("python")) # counts the number of occurrences of "python" in the string
print(a.startswith("python")) # checks if the string starts with "python"
print(a.endswith("language.")) # checks if the string ends with "language."

#split() - splits the string into a list of substrings based on a specified delimiter (default is whitespace)

sen = "Python is a powerful programming language."
words = sen.split()  # splits the string into a list of words
print(words)  # prints the list of words

#join() - joins a list of strings into a single string using a specified delimiter
join_sentence = " ".join(words)  # joins the list of words into a single string with spaces in between
print(join_sentence)  # prints "Python is a powerful programming language."   

#isalpha() - checks if all characters in the string are alphabetic
string1 = "Python"
print(string1.isalpha())  # prints True
string2 = "Python3" 
print(string2.isalpha())  # prints False

#isdigit() - checks if all characters in the string are digits
string3 = "12345"
print(string3.isdigit())  # prints True
string4 = "12345@"
print(string4.isdigit())  # prints False

#isalnum() - checks if all characters in the string are alphanumeric (letters and numbers)
string5 = "Python3" 
print(string5.isalnum())  # prints True
string6 = "Pythonm@3"
print(string6.isalnum())  # prints False
