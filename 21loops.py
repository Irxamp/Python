Varnum1=int(input("Enter a number of terms for Fibonacci Series:"))

Varn1, Varn2 = 0, 1
VarCount= 0

if Varnum1 <=0:
 print("Please enter a positive number only")
elif Varnum1==1:
 print("Fibonacci Sequence uptill",Varnum1,":")
 print(Varn1)
else:
 print("The Fibonacci Sequence:")
 while VarCount<Varnum1:
  print(Varn1)
  Vartemp=Varn1+Varn2
  Varn1=Varn2
  Varn2=Vartemp
  VarCount+=1




 