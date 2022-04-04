from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to my website"
@app.route('/gallery')
def Gallery_page():
    return "Gallery Page"


if __name__=="__main__":
    app.run()