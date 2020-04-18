d = int(input("input time in days: "))
h = int(input("input time in hours: "))
m = int(input("input time in minutes: "))
s = int(input("input time in seconds: "))
ss = d * 24 * 60 * 60 + h * 60 * 60 + m* 60 + s
print ("the total time in seconds: " , ss)