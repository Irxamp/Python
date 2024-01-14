Varnum=int(input("Enter a number:"))

Varsum=0
Vartemp=Varnum
while Vartemp>0:
 Vard=Vartemp%10
 Varsum+=Vard**3
 Vartemp//=10

if Varnum==Varsum:
 print(Varnum,"is an Armstrong number")
else:
 print(Varnum," is not an Armstrong number")





 