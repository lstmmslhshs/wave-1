t = int(input("input time in seonds: "))
d = t // 86400
h = (t-d*86400)//3600
m = (t-d*86400-h*3600)//60
s = t-d*86400-h*3600-m*60
print("It is : "+str(d)+" days"+str(h)+" hours"+str(m)+" minutes"+str(s)+" seconds")