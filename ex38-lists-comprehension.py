#list values on pi
from math import pi
i = int(input("Enter i --->"))
piList = [round(pi, i) for k in range(i)]
print(piList)
