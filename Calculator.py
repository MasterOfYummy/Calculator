print "***Dumbass Python Calculator***"
import time
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime
import math
print ">>1.Addition"
print ">>2.Subtraction"
print ">>3.Multiplication"
print ">>4.Division"
print ">>5.Square Root"
print ">>6.Factorial"
print ">>7.Straight Line Equation"
print ">>8.Prime Number Checker"
print ">>9.Quadratic Equation Solver"
print ">>10.Multiplication Table of a number"
print ">>11.Power Table of a number"
print ">>12.Roll the dice"
n1=input(">>>Enter number corresponding to desired function:")
n=int(n1)
if n==1:
    a=input(">Enter number 1:")
    b=input(">Enter number 2:")
    c=a+b
    print ">Result is:",c
elif n==2:
    a=input(">Enter number 1:")
    b=input(">Enter number 2:")
    c=a-b
    print ">Result is:",c
elif n==3:
    a=input(">Enter number 1:")
    b=input(">Enter number 2:")
    c=a*b
    print ">Result is:",c
elif n==4:
    a=input(">Enter number 1:")
    b=input(">Enter number 2:")
    c=a/b
    print ">Result is:",c
elif n==5:
    a=input(">Enter number:")
    b=a**0.5
    print ">Result:",b
elif n==6:
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    n=int(input(">Input a number to compute the factiorial : "))
    print(factorial(n))
elif n==7:
    print("Equation of a straight line")
    print("In the form - y=mx+b")
    x11=input(">>>Enter x coordinate 1:")
    x21=input(">>>Enter x coordinate 2:")
    y11=input(">>>Enter y coordinate 1:")
    y21=input(">>>Enter y coordinate 2:")
    x1=int(x11)
    x2=int(x21)
    y1=int(y11)
    y2=int(y21)
    m=(y2-y1)/(x2-x1)
    print">>Gradient=",m
    c=y1-(m*x1)
    print">>Y intercept=",c
    mp1=(x1+x2)/2
    mp2=(y1+y2)/2
    print">>Midpoint x is",mp1
    print">>Midpont y is",mp2s
elif n==8:

    num = int(input(">>Enter a number: "))


    if num > 1:

       for i in range(2,num):
           if (num % i) == 0:
               print num,"is not a prime number"
               print i,"times",num//i,"is",num
               break
       else:
           print num,"is a prime number"
    else:
        print(num,"is not a prime number")
elif n==9:
    a=float(input(">>Enter coefficient of x^2:"))
    b=float(input(">>Enter coefficient of x:"))
    c1=(input(">>Enter constant term:"))
    c=float(c1)
    d=(b**2)-(4*a*c)
    if d==0:
        print(">>One real and equal root")
    elif d>0:
        print(">>Two real and distinct roots")
    elif d<0:
        print(">>No real roots")
    m=(b*-1)
    k=(d**(0.5))
    x1=(m+k)/(2*a)
    x2=(m-k)/(2*a)
    print ">>Root 1:",x1
    print ">>Root 2:",x2
elif n==10:
    n=int(input(">>Enter number:"))
    c=int(input(">>Enter the value till which you wish to multiply:"))
    for i in range(1,c+1):
        r=i*n
        print n,"Times",i,"is",r
elif n==11:
    n=int(input(">>Enter number:"))
    c=int(input(">>Enter the value till which you wish to be powered to:"))
    for i in range(1,c+1):
        r=n**i
        print n,"to the power of",i,"is",r
elif n==12:
        import random
        min=1
        max=6
        r="yes"
        while r=="yes":
            print"Rolling the dice"
            print ">>No.1:",random.randint(min,max)
            print ">>No.2:",random.randint(min,max)
            break
