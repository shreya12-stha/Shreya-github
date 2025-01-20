# file handling is the process of handling file(.txt,.csv,etc)using programming language.
# csv(Name,age,course)
# (Shreya,20,python)


# try:
#     file = open("text.txt",'r')
#     # file.write("We are writing to the file text.txt")
#     a = file.read()
#     print(a)
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# file= open("my-text.txt",'a')
# file.write("I am learning python\n")
# file.write("We are learning more")
# file.close()

# with open("my-text.txt",'r') as file:
#     a = file.read()
#     print(a)

# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# course=input("Enter your course:")
# with open("user.info.txt",'a') as file:
#     a=file.writelines(
#         [f"{name}\n{age}\n{course}\n"]
#     )