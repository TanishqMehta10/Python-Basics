a1=int(input("Enter the number :"))
a2=int(input("Enter the number :"))
a3=int(input("Enter the number :"))
a4=int(input("Enter the number :"))
if(a1>a2 and a1>3 and a1>a4):
    print("No 1 is greater ie",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("No 2 is greater ie",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("No 3 is greater ie",a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("No 4 is greater ie",a4)

print("End of the program byeee")
# way 2 without loop
# print("from the above numbers the greatest number is",max(a1,a2,a3,a4))