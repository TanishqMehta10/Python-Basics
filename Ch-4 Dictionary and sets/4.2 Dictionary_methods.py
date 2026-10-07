marks={
    "Tanishq":99,
    "soham":95,
    "Sahil":96,
}

print(marks.keys()) #will print the keys of the dictionary ie Tanishq, soham, Sahil
print(marks.values()) #will print the values of the dictionary ie 99, 95, 96
print(marks.items()) #will print the key value pairs of the dictionary ie Tanishq 99, soham 95, Sahil 96
print(marks.get("Tanishq")) #will print the value of the key Tanishq ie 99
print(marks.update({"Akshay":98,"Harshad":99})) #will update the dictionary with new key value pairs
print(marks) #will print the updated dictionary with new key value pairs
print(len(marks)) #will print the length of the dictionary ie 3
print(dict.clear(marks)) #will clear the dictionary and make it empty
print(marks) #will print the empty dictionary
print(dict.copy(marks)) #will print the copy of the dictionary
print(dict.fromkeys(["Tanishq","soham","Sahil"],0)) #will create a new dictionary with keys from the list and values as 0
