import random
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol='(){}[];_#*._'
number='0123456789'
all=lower+upper+symbol+number
length=int(input("Enter the length of the password:"))
password="".join(random.sample(all,length))
print("The generated password is ",password)


