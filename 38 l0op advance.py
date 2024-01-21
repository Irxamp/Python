Varrows=int(input("Ener the number of rows for Pyramid:"))

for j in range(Varrows,1,-1):
 for Varspace in range (0,Varrows-j):
  print(" ",end="")
 for j1 in range(j,2*j-1):
  print("*",end="")
 for j2 in range(1,j-1):
  print("*",end="")
 print()