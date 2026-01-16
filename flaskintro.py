# FLASK INTRODUCNTION
from flask import Flask
print(__name__) # this will print main becasue that is where the initial pointer/cursor is ~~ similar to c++ and java "main"

app=Flask(__name__) # app now contains the main class using flask module

@app.route('/') #it's and API
# similar to  WHEN THE MAIN PAGE WILL BE ACCESED RUN HOME CODE
def home():
    return ("hello from flask 1")


@app.route('/about') # it's an API
# similar to when the about page is accessed, run the about code
def about():
    return ("hello jkdjask from flask 1")

    
if (__name__== "__main__"): # when found main class, run the code
    app.run()