# A list in Python stores set of values of any data types...
#You can add, remove, or change the values inside the box.
#It can hold numbers, words, or anything, and even repeat values
#in short container to store set of values..
#list can be indexed just like string..
#list are mutable ie can be changed

friend=["Apple","Orange",34,23.398,False,"Tanishq","Mehta"]
print(friend[1]) #found the index
friend[1]="Mango"
print(friend[1]) #changed the index value ie mutable
print(friend[:5]) #st to end will print the values from start to 5th index

# ****************************************
# l1=[]
# l2=[]
# a=int(input("Enter elements in l1: "))
# b=int(input("Enter elements in l2: "))
# l1.append(a)
# l2.append(b)
# l1.extend(l2)
# l1.sort()
# print(l1)

# l1 = list(map(int, input("Enter elements in l1: ").split()))
# l2 = list(map(int, input("Enter elements in l2: ").split()))

# l1.extend(l2)
# l1.sort()

# print(l1)