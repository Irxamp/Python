#calculator
what=input("what do you whant to do? (+,-,*,/)")
a=float(input("type first number "))
b=float(input("type second number "))
if what=="+":
    c=float(a+b) #4 spaces only if it is true
    print("result is "+str(c))
elif what=="-":
    c=float(a-b)
    print("result is:"+str(c))
elif what=="*":
    c=float(a*b)
    print("result is :"+str(c))
elif what=="/":
    c=float(a/b)
    print("relult is :"+str(c))
else:
    print("error")