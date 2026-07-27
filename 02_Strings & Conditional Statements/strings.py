#  \t, \n - Escape sequence character
# "this is apnacollege's tutorial"

str1 = "This is a string.\nwe are creating in python."
str2 = "This is a string.\twe are creating in python."

print(str1)
print(str2)

# Concatenation

firstName = "Om"
lastName = "Gaikwad"
fullName = firstName + " " + lastName

print(fullName)

# Length of string

len1 = len(str1)
print(len1)

len2 = len(fullName)
print(len2)

# Indexing - start from zero

str = "hello_world"
char = str[1]
print(char)

# Slicing

# str[starting_idx : ending_idx] - ending idx is not included

print(str[0:6])
print(str[6:len(str)])
print(str[:6]) # [0:6]
print(str[6:]) # [6:len(str)]
print(str[-3:-1]) # reverse indexing

# Strings function

string = "i am studying python from ApnaCollege"

print(string.endswith('ege.'))
string = string.capitalize()
print(string)
print(string.replace('ApnaCollege', 'chaiaurcode')) # str.replace('old value', 'new value')
print(string.find('python'))
print(string.find('Q'))
print(string.count('o'))
