Varnum=int(input("Enter a number to check if it is a prime number:"))

Varf=False

if Varnum > 1:
 for j in range (2, Varnum):
   if(Varnum%j)==0:
    Varf=True
   break

if Varf:
 print(Varnum, "is not a prime number")
else:
 print(Varnum, " is a prime number")