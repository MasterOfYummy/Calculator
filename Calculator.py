print "***Dumbass Python Calculator***"
import time
localtime = time.asctime( time.localtime(time.time()) )
print "Time:", localtime
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
print ">>13.Phythagorean Theorem"
print ">>14.Simple Interest"
print ">>15.Armstrong Number Checker"
print ">>16.Smallest and Largest out of entered numbers"
print ">>17.Find the sum of first n positive integers"
print ">>18.Find the sum of numbers in a given range"
print ">>19.Calendar"
print ">>20.Guess the number game"
print ">>21.Powers"
print ">>22.Random Strong Password Generator"
print ">>23.Degrees -> Radians"
print ">>24.Radians -> Degrees"
print ">>25.Math Quiz"

x=0
while x==0:
    n1=input(">>>Enter number corresponding to desired function:")
    n=int(n1)
    if n>25 or n<1:
        print(">Invalid Number<")
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
        print">>Midpont y is",mp2
        import matplotlib.pyplot as plt
        plt.plot([x1,x2],[y1,y2])
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.title("Linear Graph\nHello World")
        plt.show()
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
            break
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
    elif n==13:
        print 'Pythagorean Theorem'
        print'>1.Find Hypotenuse'
        print '>2.Find Base'
        print '>3.Find Height'
        i=0
        while i==0:
            n=int(input('Enter number corresponding to desired function:'))
            if n>3:
                print 'Invalid Input'
                continue

            h=input("Return to main menu: Y/N:")
            if h=="y":
                break
            elif h=="n":
                continue
            if n==1:
                a=float(input("Enter Base:"))
                b=float(input("Enter Height:"))
                c=((a**2)+(b**2))**0.5
                print 'Hypotenuse:',c
            elif n==2:
                b=float(input("Enter Height:"))
                c=float(input("Enter Hypotenuse:"))
                if b>c:
                    print 'Enter valid input'
                    continue
                a=((c**2)-(b**2))**0.5
                print 'Base;',a
            elif n==3:
                b=float(input("Enter Base:"))
                c=float(input("Enter Hypotenuse:"))
                if b>c:
                    print 'Enter valid input'
                    continue
                a=((c**2)-(b**2))**0.5
                print 'Height:',a
    elif n==14:
        p=float(input("Enter principle:"))
        t=float(input("Enter time:"))
        r=float(input("Enter rate:"))
        si=(p*t*r)/100
        a=si+p
        print 'Simple Interest:',si
        print 'Total Amount+Interest:',a
    elif n==15:
            num1=int(input(">Enter digit 1:"))
            num2=int(input(">Enter digit 2:"))
            num3=int(input(">Enter digit 3:"))
            num=int(input(">>Enter the number as a whole:"))
            numa1=num1**3
            numa2=num2**3
            numa3=num3**3
            sum=numa1+numa2+numa3
            if sum==num:
                print(">>The entered number is an Armstrong number.")
            else:
                print(">>The entered number is not an Armstrong number.")
    elif n==16:
        r=int(input("Enter the amount of numbers do you want to enter:"))
        largest=-1
        smallest=10000000000000000000000000000000000000000000000000000
        for i in range (1,r+1):
            num=int(input("Input number:"))
            if num>largest:
                largest=num
            if num<smallest:
                smallest=num
        print "The largest number is",largest
        print "The smallest number is",smallest
    elif n==17:
        j=int(input(">>Enter the limit:"))
        p=(j*(j+1))/2
        print ">>The sum is:",p
    elif n==18:
        n=int(input("Enter lower limit:"))
        n1=int(input("Enter upper limit:"))
        num_list = range(n, n1 + 1)
        sum=sum(num_list)
        print "The sum is:",sum
    elif n==19:
        print("**Calendar**")
        import calendar
        x=0
        while x==0:
            yy = int(input(">>Enter year: "))
            mm = int(input(">>Enter month in numbers: "))
            if mm>12 or mm<1:
                print "Invalid Number"
                break
            print(calendar.month(yy, mm))
            m=int(input("Go again? 1 for yes. 0 for no:"))
            if m==0:
                x=1
    elif n==20:
        import random
        i=random.randint(1,10)
        r=random.randint(10,20)
        n=random.randint(i,r)

        print "Lower limit:",i
        print "Upper limit:",r
        u=10
        while u>0:
            t=int(input(">>Guess the number:"))
            if t==n:
                print "Congratulations! You guessed it."
                break
            else:
                u=u-1
                print "Wrong!"
                print "Chances remaining:",u

        if u==0:
            print "Sorry. You lost."
    elif n==21:
        n=int(input("Enter number:"))
        v=int(input("Enter power:"))
        res=n**v
        print "Result:",res
    elif n==22:
        import random
        import pyperclip
        i=random.randint(1,100)
        p=random.randint(1,50)
        array1=("ho7","&j","g7#","l9R","j%","/nI")
        array2=("T5@","Gu8#","$es","F56@")
        array3=("Hu7^","We3#")
        stri=str(i)
        strp=str(p)
        array1index=random.randint(0,5)
        array2index=random.randint(0,3)
        array3index=random.randint(0,1)
        x=array1[array1index]
        y=array2[array2index]
        z=array3[array3index]
        password=stri+strp+x+y+z
        z=int(input("Enter 1 to generate a password:"))
        if z==1:
            print "Password:",password
        else:
            continue
        d=int(input("Enter 1 to copy password to clipboard:"))
        if d==1:
            pyperclip.copy(password)
    elif n==23:
        deg=float(input("Enter the value in degrees:"))
        pi=float(3.1415)
        s=float(pi/180)
        rad=float(deg*s)
        print "The result in radians is:",rad
    elif n==24:
        rad=float(input("Enter the value in radians:"))
        pi=float(3.1415)
        s=float(180/pi)
        deg=float(rad*s)
        print "The result in degrees is:",deg
    elif n==25:
        import time
        import sys
        print "**#Math Quiz#**"
        print ">>1.Noob Level"
        print ">>2.Meh Level"
        print ">>3.God Level"

        n=int(input("Input number corresponding to desired difficulty:"))
        if n>3 or n<1:
            print "Uh Oh! Looks like you can't read!"
            print "This is SO not for you!"
            time.sleep(2)
            quit()
        if n==1:
            m=0
            q1=int(input("Square root of 625:"))
            if q1==25:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            q2=int(input("What is 2342342342 raised to the power of 0:"))
            if q2==1:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            q3=int(input("What is the value of log base 10 to 100:"))
            if q3==2:
                print "Correct!"
                m=m+1
            else:
                print "Wrong!"

            q4=int(input("What is 2 to the power of 5:"))
            if q4==32:
                print "Correct!"
                m=m+1
            else:
                print "Wrong!"

            q5=int(input("What is the area of a right angled triangle with heigh 10cm and base 7cm:"))
            if q5==35:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            print "You scored",m,"out of 5"

        if n==2:
            m=0
            q1=int(input("Factorial of 4:"))
            if q1==24:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            q2=int(input("What is the value of pi radians in degrees:"))
            if q2==180:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            q3=int(input("What is the value of sin 90 degrees:"))
            if q3==1:
                print "Correct!"
                m=m+1
            else:
                print "Wrong!"

            q4=int(input("What is the real and equal root of x^2-14x+49=0:"))
            if q4==7:
                print "Correct!"
                m=m+1
            else:
                print "Wrong!"

            q5=int(input("What is the value of sin x when the opp is 3 and the adj is 4: "))
            if q5==0.6:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"
            print "You scored",m,"out of 5"
        if n==3:
            m=0
            q1=int(input("If 4 men can build a wall in 2 days, how many men can build the same wall in 1 day:"))
            if q1==8:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            q2=int(input("What is the slope of a straight line with points (1,15) & (0,9):"))
            if q2==6:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"


            q3=int(input("What is the amplitude of this function:5sin7x+90"))
            if q3==5:
                print "Correct!"
                m=m+1
            else:
                print "Wrong!"

            q4=int(input("How many combinations are there in a list of 6 numbers"))
            if q4==720:
                print "Correct!"
                m=m+1
            else:
                print "Wrong!"

            q5=int(input("What is the sin^x+cos^x-1: "))
            if q5==0:
                print "Correct!"
                m=m+1
            else:
                print "Incorrect!"
            print "You scored",m,"out of 5"
