# students=['ram','sita','hari','shyam']

# for name in students:
#     print(name)

# To print loop with messages
#     print(f"hello: {name}")

# practice 2

# numbers=[1,2,3,4,5,6,7,8,9,10]
# even numbers

# for num in numbers:
#     if num%2==0:
#       print(f"{num} is even")

# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# odd numbers 

# for num in numbers:
#    if num%2!=0:
#     print(num,end=" ")


# practices
# Q.N 1.
# students=['ram','sita','hari','gita']

# for name in students:
#     print(f"Hello:{name}")


# Q.N 2.
# numbers=[1,2,3,4,5,6,7,8,9,10]
# # even numbers?

# for num in numbers:
#     if num % 2 ==0:
#         print(num,end=" ")


# Q.N 3.
# for i in range(10):
#  print(i)

# for i in range(1,10):
#  print(i,end=" ")

# for i in range(1,10,2):
#  print(i,end=" ")


# for i in range(10,0,-1):
#     print(i,end=" ")

#Q.N 4.
# data=[12,13,6000,9000,600,8900,15000,4000,3000,10000]
# > 5000 < 10000

# for num in data:
#     if num >5000 <10000:
#         print(num)


# Q.N 5.
# enter number of times?
# enter name?

# n=int(input("enter number of times: "))
# students=[]

# for a in range(n):
#     name= input("Enter your name: ")
#     students.append(name)

# for name in students:
#     print(f"My name is {name}")


# Q.N 6
# students=[
#   {'name':'ram','address':'ktm'},
#   {'name':'shyam','address':'pokhara'},
#   {'name':'hari','address':'bhaktapur'},
#   {'name':'sita','address':'lalitpur'}
# ]
 
# for user in students:
#     print(user['name'],user['address'])


# Q.N 7
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
#         total+=mark

#     per=total/5
#     grade=" "
#     if per>=80:
#       grade="A"
#     elif per>=60:
#      grade="B"
#     elif per>=40:
#      grade="C"
#     elif per>=30:
#      grade="D"
#     else:
#      grade="F"

#     print(f"Name: {student['name']} Total:{total} Percentage:{per} Grade:{grade}")
   
    
# Q.N 8
# for x in range(1,5):
#     print(f"=========={x}==========")
#     for a in range(1,10):
#         print(a,end="")
#     print()

# Q.N 9
# find out total sum of 1 to 10 

# total=0
# for x in range(1,11):
#     total+=x
# print(total)

# Q.N 10 => total even numbers 
# total=0
# for x in range(1,51):
#     total+=x
#     if x % 2 ==0:
#         print(x)

    




# Loop control statement
# 1. pass statement => can update later when needed

# for i in range(5):
#     pass


# count=5
# while count > 0:
#     if count==3:
#         pass
#     else:
#         print(count)
#     count -=1

# 2. Break statement => Terminates the loop entirely, exiting from it immediately

# for i in range(10):
#     if i == 4:
#         break
#     print(i)

# for x in range(1,11):
#     if x==5 or x==7:
#        continue
#     print(x)

 ##Note: the loop skips when condition meet true for i==3

#  3. Continue statement => skips the current iteration and moves to the next one.

# for i in range(5):
#     if i== 4:
#         continue
#     print(i)

# print("============Student Result=============")
# num =int(input("Enter number of students: "))
# students_marks=[]
# sid=1
# while sid<=num:
#     print(f"=========Student ID: {sid}===========")
#     nep =int(input("Enter Nepali marks: "))
#     eng =int(input("Enter English marks: "))
#     math =int(input("Enter Math marks: "))
#     sci =int(input("Enter Science marks: "))
#     soc =int(input("Enter Social marks: "))
#     total = nep + eng + math + sci + soc
#     students_marks.append(total)
#     sid+=1

# print("Sid\t Total Mark \tPercentage\t Grade")
# student_id=1
# for total in students_marks:
#     per=total/5
#     grade=""
#     if per>=90:
#         grade="A+"
#     elif per>=80:
#         grade="A"
#     elif per>=70:
#         grade="B+"
#     elif per>=60:
#         grade="B"
#     elif per>=50:
#         grade="C+"
#     elif per>=40:
#         grade="C"
#     else:
#         grade="F"
#     print(f"{student_id}\t {total} \t\t{per:.2f}\t\t{grade}")
#     student_id+=1


# print("==========Student Result==========")
# print(int(input("Enter number of sutdents: ")))

# students=[]
# sid=1
# print(f"========Student ID:{sid}=========")
# student_name=int(input("Enter sutdent name:"))
# nep=int(input("Enter nepali marks: "))
# eng=int(input("Enter english marks: "))
# math=int(input("Enter math marks: "))
# sci=int(input("Enter science marks: "))
# soc=int(input("Enter social marks: "))
# total=nep+eng+math+sci+soc
# sid+=1

# # print("sid\t total mark\t percentage\t grade")

# for student in students:
#     per=total/5
#     grade=""
#     if per>=90:
#         grade="A+"
#     elif per>=80:
#         grade="A"















# product_list=[
#     {
#         "product_id": 1,
#         "product_name": "Laptop",
#         "price": 50000,
#         "quantity": 10
#     },
#     {
#         "product_id": 2,
#         "product_name": "Mobile",
#         "price": 20000,
#         "quantity": 20
#     },
#     {
#         "product_id": 3,
#         "product_name": "Tablet",
#         "price": 15000,
#         "quantity": 15
#     }

# ]
# print("==========Welcome to hamro bazar=========")
# print("1.Laptop 2.Mobile 3.Tablet")
# product_name=[]
# price=0
# quantity=0
# product=int(input("Enter your choice of product:"))

# while quantity<=product:
#     laptop=int(input("Enter laptop quantity:"))
#     mobile=int(input("Enter mobile quantity"))


