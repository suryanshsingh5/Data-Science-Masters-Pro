# Scope of a variable
abc=23
chintu=45
def greet():
    abc=3
    xyz=32
    global chintu
    print(f"local scope says that the number is: {abc}")
    print(f"local scope says that the global chintu is : {chintu}")
    print(f"i was created inside the local scope: {xyz}")
print(f"global sccope says that the number is: {abc}")
print(f"global scope says that the chintu is: {chintu}")

greet()