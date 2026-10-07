#String is a datatype in python which is used to store text data. 
#It is a sequence of characters enclosed in single quotes, double quotes or triple quotes.
#Strings are immutable ie cannot change a created string 
name = "Tanishq"

#string slicing is used to extract a part of the string using index values.
print(name[0:4])
print(name[-5:-1])
print(name[1:])

#string slicing using skip value
print(name[1:6:3]) #in this case it will print the characters at index 1 and 4 because the skip value is 3.

#more slicing techniques
print(name[:5]) #in this it will print the characters from index 0 to 4 because the end index is 5 
print(name[0:]) #in this it will print the characters from index 0 to the end of the string because the end index is not specified.
