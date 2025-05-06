# WAP to enter any age and check the person is eligable to vote or not
# 18 > = eligable to vote
# age= int(input("Enter your age: "))

# age = 20
# if age>19:
#     print ("You are eligable to vote")

# else:
#     print("You are not eligable to vote")

# practice 2
# number=13
# if number%2==0:
#     print("Even")

# else:
#     print("Odd")


# a=5
# b=12
# c=10
# if a>b and a>c:
#     print("a is greater")

# elif b>a and b>c:
#     print("b is greater")

# else:
#     print("c is greater")


# a=3
# b=10
# c=8
# d=7
# if a>b and a>c:
#     print("A")
# if b>a and b>c:
#     print("B")
# elif c>a and c>b:
#     print("C")
# else:
#     print("D")

# WAP to enter any alphabet and check if it is vowel or consonant
# a,e,i,o,u are vowels

# alpha= input("Enter an alphabet: ")
# if alpha in "aeiou":
#     print("alpha is vowel")
# else:
#     print("alpha is constonant")

# WAP to enter five subject marks and calculate total, percentage and grade.

# 80-100 -> A
# 60-80  -> B
# 40-60  -> C
# >40   -> D

# Nepali= int(input("Enter nepali marks: "))
# English= int(input("Enter english marks: "))
# Maths= int(input("Enter maths marks: "))
# Science= int(input("Enter science marks: "))
# Social= int(input("Enter social marks: "))

# # Calculating five subject marks
# total= Nepali+English+Maths+Science+Social
# per=total/5
# print("Total marks: ", total)
# print("Percentage: ", per)

# if per>80:
#     print("A")
# elif per>60:
#     print("B")
# elif per>40:
#     print("C")
# else:
#     print("Fail")

    # 1. Dell(Rs:20000) 2.HP(Rs:30000) 3. Lenovo(Rs:40000) 4. Apple(Rs:50000)
#  Enter your choice: 1
# Enter your quantity: 2
# Name


# print("=======Welcome to the store=========")
# option=int(input("choose products: "))
# option = int(input("Choose device: "))
# if option==1:
#    print("Laptop")
#    print("price for this device is: ,amount")




# WAP to enter any number and check it is divisible by 3 and 5 or not.
# number = 20
# number = 15
# if number % 3==0 and number % 5==0:
#     print("number is divisible by both 3 and 5")
# else:
#     print(" number is not divisible by both 3 and 5")



# nested if else statement

# name= input("Enter your name: ")

# if name=="admin":
#     age=input("Enter your age: ")
#     print(name)
#     print(age)

# else:
#     print("Enter your name")


# username= input("Enter your username: ")
# password= input("Enter your password: ")

# if username=="admin":
#     if password=="admin002":
#         print("Welcome to the system")
#     else:
#             print("Invalid password")
# else:
#         print("Invalid username")


# ATM balance inquiry and withdrawl process

# print("=======Welcome to ATM========")
# pin=int(input("Enter your pin: "))

# if pin==1234:
#     amount=10000
#     print("1. Check balance")
#     print("2. Withdraw cash")
#     print("3. Exit")
#     option=int(input("Select an option: "))
#     if option==1:
#         print("Your balance is",amount)
       
#     elif option==2:
#         wamount=int(input("Enter amount to withdraw: "))
#         if wamount<=amount:
#             remaining=amount-wamount
#             print("Please collect your cash")
#             print("Your withdraw balance is:",wamount)
#             print("Your remaining balance is:",remaining)
#         else:
#             print("Insufficient balance")
#     else:
#         print("Invalid option")
# else:
#     print("Invalid")




# WAP on age limits of which person can drink what kind of drinks

# age above 18 and >25 => can only drink coke
# 25-40 => can drink wine
# 40 and above can drink hard drinks

# age=int(input("Enter your age: "))
# if age>=18:
#     option=int(input("Select an option: "))
#     if age<=25:
#         print("You are eligable to drink coke")

#     if age>=25 and age<=40:
#         print("You are eligable to drink wine")
    
#     elif age>=40 and above:
#         print("You are eligable to drink hard drinks")

#     else:
#         print("You cannot drink")

# else:
#     print("Sorry, you are not eligable to drink")



# task3-> 9,6,7 > 9,7,6


# product list
# option, quantity
# if home - charge 1000
#     pickup - 500

# packing option
#     if plastic- 500
# shopping bag - 1000
# box - 1500

# location
# delivery charge
# ktm - 200
# lalitpur- 300
# bhaktapur- 500

# print bill


# print("=======Welcome to the store=========")
# option=int(input("Choose products: "))
# if option==1:
#    amount=30000
#    print("Refrigerators")
#    print("price for this product is:",amount)
#    quantity = int(input("Enter quantity: "))

# elif option==2:
#    amount=25000
#    print("Ovens")
#    print("price for this product is:",amount)
#    quantity = int(input("Enter quantity: "))
#    billamount=("price*qualtity")
#    print("bill amount")
               


# elif option==3:
#    amount=50000
#    print("Telivision")
#    print("price of this product is:",amount)
#    quantity = int(input("Enter quantity: "))


# WAP on the cost of a person who travel in bus 27km in ringroad.
# 27km
# 5-5km distance in one stop 
# rs.15 / 5km

print("=========Welcome to Bus Sewa========")
print("1. Kalanki to Swayambhu 2. Swayambhu to New buspark " \
"3. New buspark to Chabahil 4. Chabahil to Baneshwor " \
"5. Baneshwor to Dallu 6. Dallu to Kalanki")

Destination=''
per_station_cost=0
number_of_destination=0
total_cost=0

option= int(input("Enter your location: "))
if option==1:
    per_station_cost=("Rs.15")
    Destination="Kalanki to Swayambhu"
elif option==2:
    per_station_cost=("Rs.15")
    Destination="Swayambhu to New buspark"
elif option==3:
    per_station_cost=("Rs.15")
    Destination=" New buspark to Chabahil"
elif option==3:
    per_station_cost=("Rs.15")
    Destination=" Chabahil to Baneshwor"
elif option==3:
    per_station_cost=("Rs.15")
    Destination=" Baneshwor to Dallu"
elif option==3:
    per_station_cost=("Rs.15")
    Destination=" Dallu to Kalanki"
else:
    print("Invalid option")

total=number_of_destination*per_station_cost
print("==================Invoice=================")
print("Destination:",Destination )
print("per_station_cost:" ,per_station_cost)
print("number_of_destination:", number_of_destination)
print("total:", total)





# WAP on swap of number in assending order and decending order





