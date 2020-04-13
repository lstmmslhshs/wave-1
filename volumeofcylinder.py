import math
math.pi
pi = math.pi
r = input("Enter radius of cylinder: ")
h = input("Enter height of cylinder: ")
r = float(r)
h = float (h)
v = (r * r * h * pi )
print("the volume of cylinder is : " + "%.1f" % v)