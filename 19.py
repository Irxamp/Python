Varnum=int(input("Enter a number:"))

Varfact=1

if Varnum<0:
 print("Ohh sorry, Factorial does not exist for negative numbers") 
elif Varnum==0:
 print(" The Factorial of 0 is 1")
else:
 for j in range(1, Varnum+1):
  Varfact=Varfact*j
 print("The Factorial of",Varnum, "is",Varfact)
 