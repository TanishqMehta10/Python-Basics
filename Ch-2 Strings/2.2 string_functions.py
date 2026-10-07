# A string function is used to modify, check, or manipulate a string.
#string functions are also case sensitive.
# 🔹 Examples of common string functions:

name = "Tanishq"
print(len(name))
print(name.endswith("shq"))
print(name.upper())
print(name.lower())
print(name.startswith("Tan"))
print(name.replace("a", "x"))
print(name.count("a"))
print(name.find("n"))
print(name[::-1]) #in this it will print the string in reverse order. as : means start from the end and -1 means go backwards by 1 step.
print(name[0:4]) #in this it will print the characters from index 0 to 3 because the end index is 4. The end index is not included in the output.

# What it does (simple):
# len() → length
# endswith() → checks ending
# upper() / lower() → case change
# startswith() → checks starting
# replace() → replace letters
# count() → count letters
# find() → index of letter
# [::-1] → reverse
# [0:4] → slicing