def funcadd(Varx, Vary):
 return Varx+Vary

def funcsub(Varx, Vary):
 return Varx-Vary

def funcmul(Varx, Vary):
 return Varx*Vary

def funcdivide(Varx, Vary):
 return Varx/Vary

print("Please select the operator:")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
 Varch=input("Enter the Choice(1/2/3/4):")

 if Varch in('1','2','3','4'): 
  Varno1=float(input("Enter first Number:"))
  Varno2=float(input("Enter Second Number:"))

  if Varch=='1':
   print(Varno1,"+",Varno2,"=",funcadd(Varno1,Varno2))
 
  elif Varch=='2':
   print(Varno1,"-",Varno2,"=",funcsub(Varno1,Varno2))
  
  elif Varch=='3':
   print(Varno1,"*",Varno2,"=",funcmul(Varno1,Varno2))
  
  elif Varch=='4':
   print(Varno1,"/",Varno2,"=",funcdivide(Varno1,Varno2))
  break
 else:
  print("Invalid Input")

  









 