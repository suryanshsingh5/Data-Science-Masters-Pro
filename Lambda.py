# Lambda Function

def square ( x ):
    return x*x

SquareNumber = lambda x : x*x
SquareNumber ( 85 )

( lambda x,y : x+y ) ( 4,6)
( lambda x : x[ 1 ]) ( "mayank")


ifelselambda = lambda x: x**2 if ( x%2 == 0 ) else x**3
ifelselambda ( 4 ), ifelselambda ( 9 )