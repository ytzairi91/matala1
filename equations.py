

def exponent(x:float):
    p=float(1)
    intX=x
    result=float(1)
    factorial=int(1)
    while(intX>p-200):
        factorial= factorial * p
        p=p+1
        result= result+ x/factorial
        x=x*intX
        a = float('%0.6f' % result)
    return a



  
def ln(x:float):
    if (x<=0):
        return print('wrong input')
    
    elif(x>0 and x<1):
        y=float(0)
        p=0
        while(x>p):
            p=p+x/2
            intY=y
            y=  intY+2*(x -exponent(intY))/(x+exponent(intY))
        return y
    elif(x>=1):
        y=float(0)
        p=0
        
        while(x>p):
            p=p+1
            intY=y
            y=  intY+2*(x -exponent(intY))/(x+exponent(intY))
        return y
        



def XtimesY(x:float,y:float):
    if(x==0):
        return 0
    elif (y==1):
        return x
    
    else:
        return exponent(y*ln(x))
     
        
        
def sqrt(x:float,y:float):
    if(y<0):
        return print('wrong input')
    else:
        return XtimesY(y, 1/x)


def calculate(x:float) :
    if(x<0):
        return 0
    else:
        num= exponent(x) * XtimesY(7, x) * XtimesY(x,-1) * sqrt(x,x)
        return num 


a=float(input('enter a number:',))  
print(calculate(a))
