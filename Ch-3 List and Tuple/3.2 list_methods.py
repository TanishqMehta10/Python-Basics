friends=["Apple","Orange",34,23.398,False,"Tanishq","Mehta"]
print(friends)

#append method adds the value at the end of the list
friends.append("Chronicle of Narnia") 
print(friends)

l1=[1,13,1032,23,45,67,89]
l1.sort() #sort method sorts the list in ascending order
print(l1)

l2=[2,34,32,56,61,45,98,22,45]
l2.reverse() #reverse method reverses the list
print(l2)

l3=[1,2,3,4,5,6,7,8,9]
l3.insert(2,100) #insert method inserts the value at the given index
print(l3)

l4=[9,8,7,6,5,4,3,2,1]
l4.remove(5) #remove method removes the value from the list
print(l4)

l5=[1,2,3,4,5,6,7,8,9]
l5.pop() #pop method removes the last value from the list
print(l5)

l10=[1,2,3,4,5,6,7,8,9]
l10.pop(2) #pop method removes the value at the given index
print(l10) 
 
l6=[1,2,3,4,5,6,7,8,9]
l6.clear() #clear method removes all the values from the list
print(l6)

l7=[1,2,3,4,5,6,7,8,5,9]
l7.count(5) #count method counts the number of occurrences of a value in the list
print(l7.count(5))

l8=[1,2,3,4,5,6,7,8,9]
l8.index(5) #index method returns the index of the first occurrence of a value in the list
print(l8.index(5))

l9=[1,2,3,4,5,6,7,8,9]
l9.insert(2,100) #insert method inserts the value at the given index first is the index and second is the value to be inserted
print(l9)