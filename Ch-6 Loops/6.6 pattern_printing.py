#print star vertically
for i in range(5):    
    print("*")
    
#print star horizontally
for i in range(5):    
    print("*",end="")   #end="" means after printing, don't move to the next line.
    
    
#print star pattern by taking user input of n
n=int(input("Enter value of num: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("") 