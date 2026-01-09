# Variable Length Arguement

def sum ( a, b, d=56 ):
    c= a+b+d
    print(f" the output is sum of a={ a } and b={b} and d={d}= {c}")
sum ( 34,343)
sum ( b= 34, a= 3443, d=343) 

def Mysum ( a, b ): 
    c= a+b
    print(f" the output is Mysum of a={ a } and b={b} = {c}")
Mysum ( 34,343) 
Mysum ( b= 34, a= 3443) 


def myBestSum( a,b,c):
    print(f" the output is myBestSum of a={ a } and b={b} = {a+b}")
myBestSum(2,3,7)
myBestSum(2,3,4)

# Selecting Multiple Data into one variable
def myBestProSum( *numbers ):
    ans =0
    for i in numbers:
        ans+= i
    print ( f"The sum of all the provided numbers is : {ans}")
    print (f"All Numbers were : { numbers}")
myBestProSum(1,2,3,4,5,6,7)

def myProduct( *numbers,divisor):
    
    for i in numbers:
        print(i)

    print("The divisor is : " , divisor)
myProduct(1,2,33,4,5,6,77,8,[8,90,76565],divisor=4)

# Keyword Arguements
def myDicFun(**kwarg):
    print( kwarg)
    for k,v in kwarg.items():
        print(f" {k}:{v}")
myDicFun(first=23, sec=354)