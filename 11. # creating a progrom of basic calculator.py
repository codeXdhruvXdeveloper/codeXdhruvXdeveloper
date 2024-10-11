# creating a progrom of basic calculator 

a=input("Please type in the math operation you would like to complete:\n+ for addition\n- for subtraction\n* for multiplication\n/ for division : ")+
b=int(input("enter 1st no: "))
c=int(input("enter 2nd no: "))
if(a=='+'):
    print("addition of",b,"amd",c,"is",b+c)
elif(a=='-'):
    print("subtraction of",b,"amd",c,"is",b-c)
elif(a=='*'):
    print("multiplication of",b,"amd",c,"is",b*c)    
elif(a=='/'):
    print("division of",b,"amd",c,"is",b/c)
else:
    print("wrong input")