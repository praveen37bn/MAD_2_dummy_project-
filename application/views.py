from flask import current_app as app

@app.get('/')
def home():
    return "<h>Hello world form html h tags </h>"


    