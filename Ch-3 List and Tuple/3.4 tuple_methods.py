a=(1,3,443,False,"Tanishq","QWERT")
print(a)

# count method counts the number of occurrences of a value in the tuple
t1=(1,2,3,4,5,2,6,2,7,8)
print(t1.count(2))


# index method returns the index of the first occurrence of a value in the tuple
t2=(1,2,3,4,5,6,7,8,9)
print(t2.index(5))


# index method can also be used with a starting index
# first is the value to search and second is the starting index
t3=(1,2,3,4,5,2,6,2,7,8)
print(t3.index(2,1)) # will return the index of the first occurrence of 2 after index 1


# index method can also be used with a starting and ending index
# first is the value, second is the starting index and third is the ending index
t4=(1,2,3,4,5,2,6,2,7,8)
print(t4.index(2,2,8)) # will return the index of the first occurrence of 2 between index 2 and 8

t5=(10,20,30,40,50)
# len() returns the number of elements in the tuple
print(len(t5))


t6=(10,20,30,40,50)
# accessing an element using index
print(t6[2])


t7=(10,20,30,40,50)
# negative indexing
print(t7[-1])


t8=(1,10,20,30,40,50,67,89,90)
# slicing returns a part of the tuple
print(t8[0:4])


t9=(10,20,30,40,50)
# checking whether a value exists in the tuple
print(30 in t9)


t10=(10,20,30)
# concatenation joins two tuples
t11=(40,95,60)
print(t10 + t11)


t12=(1,2,3)
# repetition repeats the tuple multiple times
print(t12 * 3)