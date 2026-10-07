#A collection of key value pairs.
#unordered meaning the order of the items is not guaranteed to be preserved.
#mutable meaning you can change the values inside the dictionary.
#dictionaries are indexed meaning you can access the values using keys instead of index numbers.
#dictionaries are defined using curly braces {} and key-value pairs are separated by a colon :.
#the keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while the values can be of any data type and can be duplicated.
#the values in a dictionary can be of any data type, including other dictionaries, lists, or even functions.
#dictionaries are useful for storing and retrieving data in a structured way, and they are commonly used in many programming tasks, such as data analysis, web development, and machine learning.
#dictionaries are better than lists when you need to look up values based on a key, as they provide faster access times compared to searching through a list.
marks={
    "Tanishq":90,
    "Rohit":89,
    "Ramesh":78,
    "Gaurav":99
    }
print(marks,(type(marks)))
print(marks["Tanishq"],(type(marks))) #accessing the value using key

# d={} ->its a empty dictionary