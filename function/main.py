# what is function?
# function is a block of code that only that only runs when it is called
# there are two types of functions
# built-in functions
# user-defined function

# # def hello():
#     print("Hello Python!")

# hello()

# 2.
# def hello(name):
#     print("Hello",name,"!")

# hello("Python")
# hello("Dotnet")

# 3. WAP to enter three number and print sum 
# def add(a,b,c):
#     print(a+b+c,)

# add(5,6,7)

# 4.WAP on students total marks,per,grade: ask to enter marks to the user
# def result(nep,eng,math,sci,soc):
#  marks=[]
   
# nep =int(input("Enter Nepali marks: "))
# eng =int(input("Enter English marks: "))
# math =int(input("Enter Math marks: "))
# sci =int(input("Enter Science marks: "))
# soc =int(input("Enter Social marks: "))
# total=('nep+eng+math+sci+soc')

# def calculate_total(marks):
#  return sum(marks)

# for total in marks():

#  per=[]
# def calculate_per(total,num_subject):
#  return total/num_subject

 
# def grade():""
 
# if  per >= 90:
#     grade ="A+"
# elif per >= 80:
#     grade ="A"
# elif per >= 70:
#     grade ="B+"
# elif per >= 60:
#     grade ="B"
# elif per >= 50:
#     grade ="C+"
# elif per >= 40:
#     grade ="C"
# else:
#     grade ="F"

# print(f"Total Marks: {total}")
# print(f"Percentage: {per:.2f}%")
# print(f"Grade: {grade}")


 

 
 

#  5. 
# def total(p1,*num):
#   print(num)
#   print(p1)
#   pass

# total(45,79,89,90,67)

# 6. WAP to enter three number and find the smallest number


# practice
def take_value():
  p=10
  t=10
  r=10
  return [p,t,r]

def calculate():
  p,t,r=take_value()
  return p*t*r/100

def display():
  print("The simple interest is: ",calculate())

  display()




