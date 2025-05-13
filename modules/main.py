# diff ways of print:
# 1.
# import calculator
# print(calculator.add(3,5))

# 2.
# import calculator as cal
# (print(cal.add(3,5)))

# 3.
# from calculator import add
# print(add(3,5))

# it does'nt need to import from calcilator.py to run this
# if __name__=="__main__":
#     print("Hello")

import datetime
# today = datetime.date.today()
# print(today)

# date ="2023-10-01"
# date = datetime.datetime.strptime(date, "%Y-%m-%d")

import datetime
jobs =[
    {'title':"python developer", "exp_date":"2024-04-25"},
    {'title':"java developer", "exp_date":"2024-04-25"},
    {'title':"data analyst", "exp_date":"2024-04-25"},
    {'title':"data scientist", "exp_date":"2024-04-25"},
    {'title':"web developer", "exp_date":"2024-04-25"},
    {'title':"android developer", "exp_date":"2024-04-25"},
]

def expired_jobs(jobs):
    for job in jobs:
        if job ['exp_date'] < str(datetime.date.today()):
            print(f"{job['title']} -> {job['exp_date']}")
        else:
            print(f"{job['title']} -> not expired ")

expired_jobs(jobs)







# import os
# print(os.getcwd())
# os.mkdir('users')


# import math
# import datetime
# import random
# import os
# import sys