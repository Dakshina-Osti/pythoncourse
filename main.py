# print ("Hello World")
# print(345)

# print("Hello python",345,"hello")

# x=564
# y=37
# a=x+y
# print(a)

# name ="Hari"
# age =45
# adress ='ktm'
# print(name,age,adress)

# name =input("Enter your name: ")
# age =input("Enter your age: ")
# email =input("Enter your email: ")
# adress =input("Enter your adress: ")
# phone =input("Enter your phone: ")
# country =input("Enter your country: ")

# print("my name is", name)
# print("my age is", age)
# print("my email is", email)
# print("my adress is", adress)
# print("my phone is", phone)
# print("my country is", country)


# name =input("Enter your name: ")
# age =input("Enter your age: ")
# email =input("Enter your email: ")
# adress =input("Enter your adress: ")
# phone =input("Enter your phone: ")
# country =input("Enter your country: ")

# # print("my name is {} age {} email {} adress{} phone {} country {}" .format(name,age,email,adress,phone,country)) - 
# print(f"my name is {name} age{age} email{email} adress{adress} phone{phone} country{country} ")


# x= int(input("Enter x: "))
# y= input("Enter y: ")
# y= int(y)
# print(x+y)

# nepali= int(input("nepali: "))
# english= int(input("english: "))
# math= int(input("math: "))
# science= int(input("science: "))
# social= int(input("social: "))


# print(nepali+english+math+science+social)
# print(f"{part} is {percentage}% of {whole}")

# nepali,english,math,science,social
# total,percentage 

# *Day-2
# a,b,*c=12,40,14,20,30
# print(a)
# print(b)
# print(c)

# *slicing
# name="sophia"
# # print(name[-2])
# print(name[3:])

# float
# a=0123456.2536
# print(type(a))

# a=45+75j    
# print(a.real)
# print(a.imag)


# course='we are learning python'
# print(course.lower())
# # print(dir(course))
# # print(course[3:13])

# course='we are learning python'
# print(course.upper())

# a=True
# print(type(a))
# print(5>8)
# print(5<8)

# Day-3
# =>String is a sequence of character
# course ="we are learning python"
# # =>strip remove unnecessary commas, space 
# print(course.strip())

# new = course.split(' ')
# print(new)
# print(new[1])

# title,lower,upper,strip,replace,split,capatilize

# 2. Non-primetive data types : list, tuple, dictionary, set

# What is list?
# =>list is a collection of items in a particular order
# =>list is mutable( Changabale)
# =>list is defined by square brackets
# =>list index start from 0
# =>list can have any data type
# =>list can have duplicate values eg. data=[12,13,12]
# print(data)
# =>list can be nested

# data=["ram",223,"hari",True]
# print(data[2])
# print(len(data)) =>length of data/how many numbers are included in data
# data[0]="sophia"
# print(data)
# print(data[10])

# data["ram"]
# data[0]='hari'
# print(data)

# data=[]
# data=['laxmi']
# data.append('ram')
# data.append('hari')
# print(data)

# user=[]
# name=input("Enter your name: ")
# email=input("Enter your email: ")
# adress=input("Enter your adress: ")
# user.append(name)
# user.append(email)
# user.append(adress)
# print(user)

# matrix
# data=[
#     5000, 3000,
#     [1,2,3,4,5],
#     [8,9,6]
# ]
# print(data)
# print(data[3][1])
# # print(data[2][1])

#  data[]
# print(dir(data))

# Day-4-> list practice
# ()=> tuple ( cant change index value)
# data=[
#     [10,20,30,40,50],
#     [45,67,[[9000],8000,[[[340000],50000]],12000],78,30]
# ]
# print(data[1][2])
# print(data[1][2][1])
# print(data[1][1])
# print(data[1][2][2][0][0][0])
# print(data[1][3])
# print(data[1][4])
# print(data[1][2][2][0][1])
# print(data[1][2][3])

# data[1][2][2][0][0].append(1000)
# data[1].append(7000)
# print(data)

# data[0].append(1000)
# data[1].insert(3,1000)
# print(data)

# set=> {didnt assign duplicate Value}
# data={1,2,1,3,3}
# print(data)

# dictionary=> {human Readable key,user friendly}
# data={
#     "name": "ram",
#     "age": 20
# }
# print(data["name"])
# print(data["age"])

# user={
#     "name": "ram",
#     "contact":{
#         "phone": 9840266946,
#         "email": "panchi6249@gmail.com"
#     }
# }
# print(user['contact']['phone'])

# eg :- list data and dictionary data type
# data=[
#     {"name": "Ram"},
#     {"name": "Sita"}
# ]
# print(data[0]["name"])
# print(data[1]["name"])

# research => operators in python








