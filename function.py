# function= a block of code which only runs when it is called

# in python function definition and function declaration
# function definition
# function declaration
# function call 

# signature of function 
# def sum(x,y) 

# def sum(x,y):x,y parameter
#     x=10
#     y=20
#     print(x+y)

# sum

# sum(10,20) 10,20 argument

# def diff():
#     a=30
#     b=10
#     diff=a-b
#     print(diff)
# diff()

# def information(fname,lname):
#     print(f"{fname}{lname}")
# first_name=input("Enter first_name: ")
# last_name=input("Enter last_name: ")
# information(first_name,last_name)

# requirement
# first_number,last_number
# addition
# subtraction
# division 
# multiplication
# choice
# +,-,/,*

# def calculate():
#     first_number=int(input("Enter first_name:"))
#     last_number=int(input("Enter last_number:"))
#     print("Enter + for addition")
#     print("Enter - for subtraction")
#     print("Enter / for division")
#     print("Enter * for multiplication")
#     choice=input("Enter your choice:")
#     if choice=="+":
#         num=first_number + last_number
#         print("sum is",num)
#     elif choice=="-":
#         num=first_number-last_number
#         print("difference",num)
#     elif choice=="/":
#         num=first_number/last_number
#         print("division",num)
#     elif choice=="*":
#         num=first_number * last_number
#         print("multiplication",num)
#     else:
#         print("No choice")
    
# calculate()

# def sub(a,b):
#     sub=a-b
#     return sub

# print(sub(50,25))

# positional argument and keyword or named argument

# positional argument
# def info(fname,lname):
#     print(fname,lname)
# info("shreya","shrestha")

# named_argument
# info(lname="shrestha",fname="shreya")

# arbitary argument(*args) and keyword arguemts(**kwargs)

# def number(a,b,*args):
#     print(a,b,args)
#     for i in args:        (Tuple is used)
#         print(i)

# number(1,2,3,5,7,9)

# def information(**kwargs):
#     print(kwargs["fname"])

# information(fname="shreya",lname="shrestha",age="20",college="Birendra",grade="3rd semester")

# def information(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value) 
# information(fname="shreya",lname="shrestha",age="20",college="Birendra",grade="3rd semester")

# def sub(a,b):
#     return a-b

# sub=diff(20,10)
# print(sub)

# sub=lambda a,b:a-b
# print(sub(20,10))

# my_list=[[(1,2,3),20],[(4,5,6),10],[(6,7,8),2]]
# my_list.sort(key=lambda item:item[1])
# print(my_list)