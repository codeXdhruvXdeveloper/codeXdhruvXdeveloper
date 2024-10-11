#understanding the working of if else conditions in python 
# creating a program where we find greatest no between two nos.
a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
if(a>b): # here we are checking that a is greater than b  then print this is a greatest no 
    print(a,"is a greatest no.")
elif(a<b): # here we are checking that b is greater than a  then print this is a greatest no 
    print(b,"is greatest no.")
else: # here if upper conditons not fulfill then print wrong input
    print("wrong input")
