#__author: yaomingxi
#__date: 2019-04-15

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

print(name,age,job,salary)

msg ='''

---------- info of %s ---------

name: %s
age : %s
job : %s
salary : %s

You will be retired in %s years

------------ end -------------

''' % (name,name,age,job,salary,65 - int(age))

print(msg)