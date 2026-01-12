# Try Except
a = int(input("enter the number a: "))
b = int(input("enter the number b: "))
try: 
    print ( a/b )
except: 
    print( "there is and error \nit seems that there is zero")


# catching the error
a = int(input("enter the number a: "))
b = int(input("enter the number b: "))
try: 
    print ( a/b )
except Exception as e:
    print(e)
              