# l=[1,23,3434,34323,54]
# for i in l:
#     print(i)

# range(start, stop, step): syntax for for_loop

for i in range(1,10,2):
    print(i)
    
# using to print a string 
name = "Tanishq"

for ch in name:
    print(ch)
    
#find a character in a string 
name = "Tanishq"

for ch in name:
    if ch == "a":
        print("Found")
        
#iterating it in a list 
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)
    
#finding sum of list 
l=[1,33,22,54,32]
total=0
for i in l:
    total=total+i
print(total)

#finding largest no in list 
li=[32,545,2,67,887,9,0,1234]
largest=numbers[0]
for i in li:
    if i>largest:
        largest=i
print(largest)



#counting even no in a list 
liist=[12,23,34,23,22,11,10,56,678,98,64]
count=0
for i in liist:
    if i%2==0:
        count+=1
print(count)

#searching a element
ele=[1,2,3,4,5,6]
target=4
for i in ele:
    if i==target:
        print("Target Found")
        
        
#printing a multiplication table 
for i in range(5,51,5):
    print(i)
    

#for with else
l=[1,2,4,6]
for item in l:
    print(item)

else:
    print("done")
    
    
#iterate using index
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(i, numbers[i])
    
#write same in diff way as 
numbers = [10, 20, 30]
for i, num in enumerate(numbers):
    print(i, num)