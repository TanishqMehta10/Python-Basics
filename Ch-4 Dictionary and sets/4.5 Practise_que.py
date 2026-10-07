#create  dict og hindi words as eng tranl give user option to look
words= {
    "madat":"help",
    "bhukkad":"hungry",
    "harami":"rascal",
}
word=input("Enter words you want meaning of: ")
# print(words[word])
print(words.get(word,"word not found")) #will print  the meaning of the word if it exists in the dictionary, otherwise it will print "word not found"


#input  num from user and display all unique once
s=set() #creating an empty set
n=int(input("Enter the no to add in set :"))
s.add(n)
n=int(input("Enter the no to add in set :"))
s.add(n)
n=int(input("Enter the no to add in set :"))
s.add(n)
n=int(input("Enter the no to add in set :"))
s.add(n)
n=int(input("Enter the no to add in set :"))
s.add(n)
n=int(input("Enter the no to add in set :"))
s.add(n)
print(s)

#check can we print any no as a string as well as a int in set 
se=set()
n=int(input("Enter the no to add in set "))
a=input("Enter no to add in set ")
se.add(n)
se.add(a)
print(se) #it will print the no as a string and int both as they are different data types

##create empt dict allow 4 frnd to enter fav lang as values and use key as name assume names are unique.
d={}
name=input("Enter your name :")
language=input("Enter your fav lang :")
d.update({name:language})
# d[name]=language
name=input("Enter your name :")
language=input("Enter your fav lang :")
d.update({name:language})
# d[name]=language
print(d) #printing the dictionary with names as keys and fav lang as values

