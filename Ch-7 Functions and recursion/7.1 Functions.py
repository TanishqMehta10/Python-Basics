#functoin is a group of statements performing a specific task
#def it is used to define a function
#there are 2 types of functions in pythons built in and user defined functions 
# in functions print It displays the answer but return sends the answer back so we can store/use it.
# Parameter → variable written while creating the function
# Argument → actual value given while calling the function

#calculation sum of two numbers 
def calc_sum(a,b):
    return sum
calc_sum(5,87)   #method 1 
calc_sum(7,89)
calc_sum(987,7)

def calc_sum(a,b):  #define parameters
    return a+b
a=int(input("Enter your no :"))
b=int(input("Enter your no :"))
print("sum is",calc_sum(a,b))

#check no is even or odd 
def check_even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
    
print(check_even_odd(5))
print(check_even_odd(987))
print(check_even_odd(122))


#using loops in function
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()

#by taking user input
def print_numbers(start, end):

    for i in range(start, end + 1):
        print(i)


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print_numbers(start, end)


#factorial of n 
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


n = int(input("Enter a number: "))

print("Factorial =", factorial(n))

