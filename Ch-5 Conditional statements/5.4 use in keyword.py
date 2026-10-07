#write code program to detect given spam words..
w1="hi"
w2="hello"
w3="bye"
w4="good morning"
message=input("Enter message to detect")
message=message.lower() #convert message to lower case so that it can detect spam words in any case
if(w1 in message or w2 in message or w3 in message or w4 in message):
    print("This is spam message")
else:
    print("This is not spam message")