import math


#
voltage1 = 170
voltage2 = 15*math.sqrt(2)
neededRatio = voltage1/voltage2
print(neededRatio)
inductance1 = 100
inductance2 = neededRatio**2*100

print(inductance2)