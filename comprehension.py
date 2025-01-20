numbers=[1,2,3,4,5,6]
# odd_numbers=[i for i in numbers if i%2==0]
# print(odd_numbers)

# numbers=[1,2,3,4,5,6,7]
# result=[i if i%2==0 else i**2 for i in numbers]
# print(result)

# dictionary comprehension
# numbers=[1,2,3,4,5,6,7]
# result={x: x**2 for x in numbers if x%2==0}
# print(result)

# result={x: "odd" if x%2!=0 else "even" for x in numbers} 
# print(result)

# result={ i for i in numbers if i % 2==0}
# print(tuple(result))

# numbers=[-2,-3,-1,0,1,2,3]
# result=["positive" if x>0 else "negative" if x<0 else "zero" for x in numbers]
# print(result)

# s="the quick fox jump over the lazy dog"
# splitted_text=s.split()
# filtered_splitted_text=list(filter(lambda x:x!='the',splitted_text))
# result=[len(word) for word in filtered_splitted_text]
# print (result)

# numbers=[
#     [-1,-2,3,9,1,2],
#     [2,3,0,-1,-2,-4],
#     [10,9,8,-8,-10,-4],
#     [2,3,4,0,-1,-2,-3]
# ]

# unique_evennumber_sum=sum({y for x in numbers for y in x if y>0 and y%2==0})
# print(unique_evennumber_sum)