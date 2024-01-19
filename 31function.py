import calendar

while True:
 
 Varyear=int(input("Enter a year which is more than 2000:"))

 if Varyear>2000:
   Varmonth=int(input("Enter a month:"))
   if(Varmonth >=1) and(Varmonth <=12):
    print(calendar.month(Varyear,Varmonth))
   else:
    print("Sorry invalid month")
   break
 else:
  print("Please enter a proper year")




  









 