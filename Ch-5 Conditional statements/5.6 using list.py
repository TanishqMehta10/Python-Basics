#find whether given username is present in list or not.
l=["Tanishq","TAM","TQ"]
name=input("Enter your name : ")

if(name in l):
    print("yes",name,"is there in list")
else:
    print("name not in list")