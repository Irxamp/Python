varside1=float(input("Enter First Side of the triangle:"))
varside2=float(input("Enter Second Side of the triangle:"))
varside3=float(input("Enter Third Side of the triangle:"))
varsemiperi=(varside1+varside2+varside3)/2
varareatri=(varsemiperi*(varsemiperi-varside1)*(varsemiperi-varside2)*(varsemiperi-varside3))**0.5
print("THe area of the Trinagle is %0.3f" %varareatri)
