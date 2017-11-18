import math

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
##x = 1432020323
##y = 134210082
##x = 14320203
##y = 13421008
##x = 1432
##y = 1342
##x = 142
##y = 134
##x = 14
##y = 13

debug = False

count = 0
def mult(x,y):
    print("Multiplying x and y...",x,"x",y)
    
    x = str(x)
    y = str(y)

    while len(x) < len(y): x = "0"+x
    while len(y) < len(x): y = "0"+y
    
    if len(x) > 1 and math.fmod(len(x),2) != 0: x = "0"+x
    if len(y) > 1 and math.fmod(len(y),2) != 0: y = "0"+y

    n = len(x)

    if len(x)>1:
        a = int(x[0:math.floor(len(x)/2)])
        b = int(x[math.floor(len(x)/2):len(x)])
    else:
        a = 0
        b = int(x) # bit of a hack?
    if len(y)>1:
        c = int(y[0:math.floor(len(y)/2)])
        d = int(y[math.floor(len(y)/2):len(y)])
    else:
        c = 0
        d = int(y) # bit of a hack?
        
    print("a:",a,"b:",b,"c:",c,"d:",d)
    if debug: pause()

    if len(str(a)) and len(str(c)) > 1:
        s1 = mult(a,c)
    else: s1 = a*c
    print("s1:",s1)
    if debug: pause()

    if len(str(b)) and len(str(d)) > 1:
        s2 = mult(b,d)
    else: s2 = b*d
    print("s2:",s2)
    if debug: pause()

    i = a+b
    j = c+d
    print("Multiplying i and j...",i,"x",j)
    if len(str(i)) and len(str(j)) > 1:
        s3 = mult(i,j)
    else: s3 = i*j
    print("s3:",s3)
    if debug: pause()

    s4 = s3-s2-s1
    print("s4:",s4)
    if debug: pause()

    print("s5_s1:",str(s1)+"0"*n)
    s5_s1 = int(str(s1)+"0"*n)
    if debug: pause()
    s5_s2 = s2
    print("s5_4:",str(s4)+"0"*math.floor(n/2))
    s5_s4 = int(str(s4)+"0"*math.floor(n/2))
    if debug: pause()
    print(s5_s1,"+",s5_s2,"+",s5_s4,"=...")
    s5 = s5_s1 + s5_s2 + s5_s4
    print(s5)
    if debug: pause()

    return s5

def pause():
    wait = input("PRESS ENTER TO CONTINUE ")
    

ans = mult(x,y)
print("mike:",ans)
print("real:",x*y)
if ans == x*y: print('success!')
else: print('failure, try again')
