Varmin=int(input("Enter the start range:"))
Varmax=int(input("Enter the end range:"))

print("Prime numbers in between",Varmin, "and",Varmax, "are:")

for Varj in range(Varmin, Varmax+1):
 if Varj >1:
  for j in range(2, Varj):
   if (Varj%j)==0:
    break
  else:
   print(Varj)
  