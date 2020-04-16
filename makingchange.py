m = int(input("input money in cents: "))
p = 1
n = 5
d = 10
q = 25
l = 100
t = 200
if m == 0 :
    print("No change is required")
if p <= m < n:
    print ("pennies: ", m)
if n<= m < d :
    nn= m/n 
    nn = int(nn)
    r1 = m%5
    print ("nickels: ", nn)
    print ("pennies: ", r1)
if d<= m < q :
    dd = m/d 
    dd = int(dd)
    r1 = m%10 
    if r1 < 5: 
        print ("dimes: ", dd)
        print ("nickels: ", "0")
        print ("pennies: ", r1)
    if r1 >= 5:
          nn= r1/n 
          nn = int(nn)
          r2 = m%5
          print ("dimes: ", dd)
          print ("nickels: ", nn)
          print ("pennies: ", r2)
if q<=m <l:
     qq=m/q
     qq=int(qq)
     r1= m%25 
     if r1 < 5: 
         print ("quarters: ",qq)
         print ("dimes: ","0")
         print ("nickels: ", "0")
         print ("pennies: ", r1)
     if  10 > r1 >= 5:
          nn= r1/n 
          nn = int(nn)
          r2 = nn%5
          print ("quarters: ",qq)
          print ("dimes: ","0")
          print ("nickels: ",nn)
          print ("pennies: ", r2)
     if r1 >= 10 :
           dd = r1/d
           dd = int(dd)
           r2 = r1%10
           nn= r2/n
           nn = int(nn)
           r3 = r2%5
           print ("quarters: ",qq)
           print ("dimes: ", dd)
           print ("nickels: ", nn)
           print ("pennies: ", r3)
if l<= m < t :
     ll=m/l
     ll= int(ll)
     r1= m%100
     if r1 < 5: 
         print ("loonies: ",ll)
         print ("quarters","0")
         print ("dimes: ","0")
         print ("nickels: ", "0")
         print ("pennies: ", r1)
     if  10 > r1 >= 5:
          nn= r1/n 
          nn = int(nn)
          r2 = nn%5
          print ("loonies: ",ll) 
          print ("quarters: ","0")
          print ("dimes: ","0")
          print ("nickels: ", nn)
          print ("pennies: ", r2)
     if  25 >r1 >= 10 :
           dd = r1/d
           dd = int(dd)
           r2 = r1%10
           nn= r2/n
           nn = int(nn)
           r3 = r2%5
           print ("loonies: ", ll)
           print ("quarters: ","0")
           print ("dimes: ", dd)
           print ("nickels: ", nn)
           print ("pennies: ", r3)
     if  r1 >= 25 :
           qq = r1/q
           qq=int(qq)
           r2 = r1%25
           dd = r2/d
           dd = int(dd)
           r3 = r2%10
           nn = r3/n
           nn = int(nn)
           r4 = r3%5
           print ("loonies: ", ll)
           print ("quarters: ",qq)
           print ("dimes: ", dd)
           print ("nickels: ", nn)
           print ("pennies: ", r4)
if  m >= t :
    tt = m/t
    tt = int(tt)
    r1 = m%200
    if r1 < 5:
          print ("toonies", tt)
          print ("loonies: ","0")
          print ("quarters","0")
          print ("dimes: ","0")
          print ("nickels: ", "0")
          print ("pennies: ", r1)
    if  10 > r1 >= 5:
          nn= r1/n 
          nn = int(nn)
          r2 = nn%5
          print ("toonies", tt)
          print ("loonies: ","0")
          print ("quarters: ","0")
          print ("dimes: ","0")
          print ("nickels: ", nn)
          print ("pennies: ", r2)
    if  25 >r1 >= 10 :
           dd = r1/d
           dd = int(dd)
           r2 = r1%10
           nn= r2/n
           nn = int(nn)
           r3 = r2%5
           print ("toonies", tt)
           print ("loonies: ","0")
           print ("quarters: ","0")
           print ("dimes: ", dd)
           print ("nickels: ", nn)
           print ("pennies: ", r3)
    if 100 > r1 >= 25 :
           qq = r1/q
           qq=int(qq)
           r2 = r1%25
           dd = r2/d
           dd = int(dd)
           r3 = r2%10
           nn = r3/n
           nn = int(nn)
           r4 = r3%5
           print ("toonies", tt)
           print ("loonies: ","0")
           print ("quarters: ",qq)
           print ("dimes: ", dd)
           print ("nickels: ", nn)
           print ("pennies: ", r4)
    if  r1 >= 100:
           ll=r1/l
           ll=int(ll)
           r2= r1%100
           qq = r2/q
           qq=int(qq)
           r3 = r2%25
           dd = r3/d
           dd = int(dd)
           r4 = r3%10
           nn = r4/n
           nn = int(nn)
           r5 = r4%5
           print ("toonies", tt)
           print ("loonies: ",ll)
           print ("quarters: ",qq)
           print ("dimes: ", dd)
           print ("nickels: ", nn)
           print ("pennies: ", r4)
    