# Self and Magic Function
class car:
    def __init__( arg1):
        print ( "hello world ! ")
        print ( type ( arg1), id(arg1))
    def sum ( a, b ):
        return a+b
c1=car()
print(type(c1))
print ( id ( c1))