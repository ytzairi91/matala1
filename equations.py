

def exponent(x:float):
    p=float(1)
    intX=x
    result=float(1)
    factorial=int(1)
    c=0
    while(c<100):           
        factorial= factorial * p
        c=c+1
        p=p+1
        result= result+ x/factorial
        x=x*intX
        a = float('%0.6f' % result)
    return a


def Ln(x:float):
    if (x<=0): 
        return float(0)  
    elif(x>0 and x<1):
        y=float(0)
        b=0
        while(x>b):
           b=b+x/2
           intY=y
           y=  intY+2*(x -exponent(intY))/(x+exponent(intY))
        return float(y)
    elif(x>=1):
        y=float(0)
        b=0
        
        while(x>b):
            b=b+1
            intY=y
            y=  intY+2*(x -exponent(intY))/(x+exponent(intY))
    return float(y)
        


def XtimesY(x:float,y:float):
    if(x==0):
        return float(0)
    elif (y==1):
        return x
    elif(x<0):
        return float(0)
    else:
        return float(exponent(y*Ln(x)))
     
        
        
def sqrt(x:float,y:float):
    if(y<=0):
        return float(0)
    else:
        return float(XtimesY(y, 1/x))


def calculate(x:float) :
    if(x<=0):
        return float(0)
    else:
        num= exponent(x) * XtimesY(7, x) * XtimesY(x,-1) * sqrt(x,x)
        return float(num)
