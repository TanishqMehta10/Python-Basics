#find whether student passed or failed if it require a total of 40% 
# and atleast 33% in each subject take input from user.

# name=input("Enter your name")
# marks1=int(input("Enter marks 1: "))
# marks2=int(input("Enter marks 2: "))
# marks3=int(input("Enter marks 3: "))
# total_percentage=(100*(marks1+marks2+marks3))/300
# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
#     print(name,"You are passed with percentage of",total_percentage)
# else:
#     print(name,"You are failed with percentage of",total_percentage)

name=input("Enter your name")
sub1=input("Enter the name of subjects :")
marks1=int(input("Enter marks 1: "))
sub2=input("Enter the name of subjects :")
marks2=int(input("Enter marks 2: "))
sub3=input("Enter the name of subjects :")
marks3=int(input("Enter marks 3: "))
total_percentage=(100*(marks1+marks2+marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 ):
    print(name,"You are passed in",sub1,sub2,sub3,"with percentage of",total_percentage)
else:
    print(name,"You are failed with percentage of",total_percentage)