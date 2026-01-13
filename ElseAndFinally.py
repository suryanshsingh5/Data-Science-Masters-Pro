# Else and Finally
class Database:
    def conn(self):
        print(" Database Connected")
    def close(self):
        print(" Database Closed")
database1=Database()
try:
    database1.conn()
    print( 123 + "abc")
    print( 1/0)
except ZeroDivisionError:
    print("")
database1.close()

# using finally statement
class Database:
    def conn(self):
        print(" Database Connected")
    def close(self):
        print(" Database Closed")
database1=Database()
try:
    database1.conn()
    print( 123 + "abc")
    print( 1/0)
except ZeroDivisionError:
    print("")
finally:
    database1.close()
