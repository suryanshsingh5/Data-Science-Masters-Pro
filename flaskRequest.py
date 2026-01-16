# FLASK AND REQUEST

#open links
from flask import Flask, url_for
print(__name__) # this will print main becasue that is where the initial pointer/cursor is ~~ similar to c++ and java "main"

app=Flask(__name__) # app now contains the main class using flask module

@app.route('/') #it's and API
# similar to  WHEN THE MAIN PAGE WILL BE ACCESED RUN HOME CODE
def home():
    #return ("Go to the <a href= '/about'> about page") # URL LINKING/ OPEN LINKS
    return f"url for {url_for('about')}"# URL LINKING/ OPEN LINKS

@app.route('/about') # it's an API
# similar to when the about page is accessed, run the about code
def about():
    return ("tHIS is now a about section.")



if (__name__== "__main__"): # when found main class, run the code
    app.run(port=8000) # we can also enter the port, it is optional