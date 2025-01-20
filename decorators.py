#  decorators=higher order function which modifies or extend the functionalities of function without changing its structure

# function as first class citizen
# it can be store in variable
# it can pass as a argument
# # it can be return as the result
 
# # verify_age()
# # age() 16 is satisfied for citizenship

# def decorator(func):
#     def verify_age(func):
#         def wrapper(a):
#             if a>=16:
#                 return func(a)
#             else:
#                 return f"{a} is not satisfied for citizenship"
#                 return wrapper 


# def name_function(a,b):
#     """"This function adds two numbers."""
#     return a+b
#     result=name_function(3,5)
#     print(f"Result:{result}")


# from sfile import access_decorator 

# # @access_decorator
# def name():
#     """This is the function to access name"""
#     pass
    

# def edu():
#     """This is the function to access edu"""
#     pass

# name()
# edu()