# i=1
# while i<=10:
#     print(i,end=" ")
#     i+=1

# i=10
# while i>=1:
#     print(i)
#     i-=1

# data=['ram','sita','gita','hari']
# print(len(data))

# i = 0
# while i<len(data):
#  print(data[i]) 
#  i+=1

# multiplication table
# number=int(input("enter a multiplication table number: "))
# i = 1
# while i <= 10:
#   print(f"{number}*{i} = {number*i}")
# i += 1
    


#  3.Remove the repeated data
# data=['ram','sita','gita','hari','gita','ram']
# new_list=[]
# for name in data:
#     if name not in neew_list:
#         new_list.append(name)
#         print(new_list)


# numbers = [ 
#         [12 , 14 , 15 , 16 , 89] ,
#         [98, 87 , 65 , 43 , 21 ]
#            ]

# for row in numbers : 
#     for num in row : 
#         print(num)
    

# students=[
#   {'name':'ram','address':'ktm'},
#   {'name':'shyam','address':'pokhara'},
#   {'name':'hari','address':'bhaktapur'},
#   {'name':'sita','address':'lalitpur'},
# ]
    
# i = 0
# while i<len(students):
#  print(f"my name is:{students[i]['name']},i live in:{students[i]['address']}")
#  i+=1


# name=input("Enter your name: ")

# while name == "":
#     print("you did not enter your name")
#     name=input("Enter your name: ")
#     print(f"Hello{name}")


# total marks, percentage and grade
# students=[
#     {'name':'ram','marks':[67,87,56,76,90]},
#     {'name':'sita','marks':[97,90,56,76,90]},
#     {'name':'gita','marks':[34,87,52,12,87]},
#     {'name':'hari','marks':[67,13,56,15,45]}  
# ]


# for student in students:
#     total=0

#     for mark in student['marks']:
#             total+=mark

#     per=total/5

#     grade=""
#     if per>=80:
#         grade="A"
#     elif per>=60:
#         grade="B"
#     elif per>=40:
#         grade="C"
#     elif per>=30:
#         grade="D"
#     else:
#         grade="F"

#     print(f"Name:{student['name']} Total:{total} Percentage:{per} grade:{grade}")


#  even number for 1 to 50
 
# total=0
# for x in range(1,51):
#     if x%2==0:
#         total+=1

# print(total)


# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sophia','gender':'female','status':False},
#     {'name':'gopal','gender':'male','status':False},
#     {'name':'hari','gender':'male','status':False},
#     {'name':'sita','gender':'female','status':True},

# ]
# total users
# total male
# total female
# total active users
# total inactive users
# total active male
# total active female
# total inactive male
# total inactive female


# practice 2

category=[
    {'cid':1,'name':'laptop'},
    {'cid':2,'name':'mobile'},
    {'cid':3,'name':'tv'},
]


products=[
    {'pid':1,'cid':1,'name':'dell','price':50000,'qty':10},
    {'pid':2,'cid':1,'name':'mac','price':90000,'qty':8},
    {'pid':3,'cid':2,'name':'mi','price':20000,'qty':60},
    {'pid':4,'cid':3,'name':'sony','price':15000,'qty':30},

]
# result should be:
# category: laptop
#     name: dell
#     name: mac
# catagory: mobile
#     name: mi

product_name=0
product_price=0
product_qty=0

for cat in category['cid'],['name']:
  category+=0

  for prod in products['pid'],['cid'],['name'],['price'],['qty']:
    product+=0

else:
    pass









