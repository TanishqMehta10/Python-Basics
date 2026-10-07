#Q1.Write a program to print the name of user and great them as good afternoon  
name=input("Enter your name :")
print(f"Good afternoon,{name}")
print("Good afternoon",name)

#q2.use .replce fun
# letter = ''' Dear <|NAME|>,
#              YOU ARE SELECTED
#              <|date|> '''
             
# print(letter.replace("<|NAME|>","Tanishq").replace("<|date|>","2 July 2026"))

#q3.find doule space in string ie use.find method
name = "Tanishq Mehta is   a cool coder"
print(name.find(" "))