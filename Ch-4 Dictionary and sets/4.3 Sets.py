#Set is a collection of unordered and unindexed elements (cannot access elements using index numbers)  
# It is a mutable data type in Python. 
# Sets are defined by enclosing elements in curly braces {} or by using the built-in set() function.
#sets are useful for performing mathematical operations such as union, intersection, and difference.
#Sets cannot contain duplicate elements, meaning that each element in a set is unique. If you try to add a duplicate element to a set, it will be ignored.

s={1, 2, 3, 4, 5}
print(s, (type(s))) #printing the set and its type

# empty_set=set() #creating an empty set using set() function
#a set will count a value only once even if it is repeated multiple times in the set
s1={1,5,2, 3, 4, 5, 1, 2,7,3}
print(s1, (type(s1))) #printing the set and its type  

s1.add(6) #adding a new element to the set
print(s1) #printing the updated set

s1.copy() #creating a copy of the set
print(s1) #printing the copied set

s1.clear()
print(s1) #printing the cleared set which is now empty

s3 = {9,8,7,6,5}
s4 = {6,5,4,3,2}

print(s3.difference(s4)) #printing the difference of two sets s3 and s4
print(s4.difference(s3))  

print(s3.intersection(s4)) #printing the intersection of two sets s3 and s4
print(s3 & s4) #printing the intersection of two sets s3 and s4 using & operator

