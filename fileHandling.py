# open a file
file = open("newFile.txt", "w")
file.write("""""
so, hello everyone
this is the new file that i have created
""")
file.close()

file = open("newFile.txt", "r")
file.read()
file.readlines()
file.readline()
file.close()

file = open("newFile.txt", "w")
file.truncate(250)
file.close()