#write mul table using for by taking input from user 
a=int(input("Enter your number"))
for i in range(1,11):
    print(a*i)


#print mul table in reverse order 
n = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(n * i)
    
#write a program to fetch list name starting with s
l=["Tanishq","Soham","Steven strange","Mehta"]
for name in l:
    if name.startswith("S"):
        print(name)
        

#write program to find whether no is prime or not 
n=int(input("Enter your number:"))
for i in range(2,n):
    if n%i==0:
        print("No is not prime")
        break
else:
    print("No is prime")
    
#check prime no betn 1 to 20 
for num in range(1,21):
    for i in range(2,num):
        if num %i ==0:
            break
    else:
        print(num)
    

#find sum of first n natural no 
n=int(input("Enter your number :"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)


#find fact of given no 
n=int(input("Enter you number: "))
product=1
for i in range(1,n+1):
    product = product*i
print(product)