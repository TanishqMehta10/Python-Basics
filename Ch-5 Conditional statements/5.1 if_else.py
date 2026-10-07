#check eligible to vote or not 
a=int(input("Enter your age : "))
b=input("Enter your name : ")
if(a>=18):
    print("You can vote", b)
elif(a<=0):
    print("You entered invalid age",b)
else:
    print("You cannot vote",b)